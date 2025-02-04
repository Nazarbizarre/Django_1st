from django.shortcuts import render

items = {
  "Doctor": {
    "id": 1,
    "description": "Other congenital malformations of heart",
  }, 
  "Good": {
    "id": 2,
    "description": "Drowning and submersion due to falling or jumping from unspecified burning watercraft, initial encounter",
  }, 
  "Bad": {
    "id": 3,
    "description": "Foreign body in other and multiple parts of external eye, unspecified eye, sequela",
  }, 
  "Great": {
    "id": 4,
    "description": "Other specified osteochondropathies, unspecified lower leg",
  },
}



def items_list(request):
    return render(request, "index.html")
  
  
 