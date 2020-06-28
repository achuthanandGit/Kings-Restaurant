from django.core.mail import send_mail
from django.conf import settings

from ..models import RestaurantMenu, FoodCategory, FoodSubCategory

"""
group_menu_list is used to group the food menu according to the categories and sub-categories.

return as follows
temp_food_menu_list = {
    category : {
        sub-category: [list of RestaurantMenu Model data]
    }
}

"""
def group_menu_list(restaurant_menu_list):
    #variable to save final changes
    food_menu_list = {}

    # getting category data
    category_list = FoodCategory.objects.all()
    # getting sub-category data
    sub_category_list = FoodSubCategory.objects.all()

    # grouping food menu according to category data
    for category in category_list:
        category_wise_list = restaurant_menu_list.filter(category=category.id)
        sub_category_sub_list = sub_category_list.filter(category=category.id)
        sub_list = {}
        # grouping food menu according to sub-category data
        for sub_category in sub_category_sub_list:
            sub_category_wise_list = restaurant_menu_list.filter(category=category.id, sub_category=sub_category.id)
            sub_list.update({sub_category.name : sub_category_wise_list})
        food_menu_list.update( {category.name : sub_list} )
    return food_menu_list

"""
arrange_food_menu is used to re-arrange menu list to display in the template

returns as follows
resulatant_dic = {
    row0 : [
        {
            category : {
                sub-category : []
            }
        },
        {
           category : {
                sub-category : []
            } 
        }
    ]
}
"""
def arrange_food_menu(food_menu_list):
    # variable to save final changes
    resulatant_dic= {}
    # index variable is used to track the positions of category data in food_menu_list
    index = 0
    dic_length = len(food_menu_list)
    range_length = 0

    # to determine how many rows are required
    if dic_length % 2 == 0:
        range_length = dic_length/2
    else:
        range_length = int(dic_length/2) + 1
    dic_key_list = list(food_menu_list)
   
    # creating rows with 2 columns. Each column will have one category food items with category as title
    for i in range(int(range_length)):
        dict1 = {}
        dict2 = {}
        dict1.update( {dic_key_list[index] : food_menu_list[dic_key_list[index]]} )
        index+=1
        if(index < len(food_menu_list)):
            dict2.update( {dic_key_list[index] : food_menu_list[dic_key_list[index]]} )
            index+=1
            resulatant_dic.update(
                {
                    "row"+str(i) :[dict1, dict2]
                }
            )
        else:
            resulatant_dic.update(
                {
                    "row"+str(i) :[dict1]
                }
            )
    return resulatant_dic

        

