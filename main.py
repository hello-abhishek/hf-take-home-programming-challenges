from recipe_job import run, sink_to_csv, recipes, top_ten, sort_by_rating

if __name__ == '__main__':
    run()
    sink_to_csv(recipes)
    # sort_by_rating(recipes)