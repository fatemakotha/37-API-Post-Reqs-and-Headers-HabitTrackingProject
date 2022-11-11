#UPDATE A PIXEL: USING requests.put()

pixela_endpoint_update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today_format_changed}"

update_params = {
    "quantity": "29",
}

update_pixel = requests.put(url=pixela_endpoint_update_pixel, json=update_params, headers=headers)
print(update_pixel.text)

#...............................................................................................................................

#DELETE A PIXEL: USING requests.delete()

pixela_endpoint_delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today_format_changed}"

delete_pixel = requests.delete(url=pixela_endpoint_delete_pixel, headers=headers)
print(delete_pixel.text)