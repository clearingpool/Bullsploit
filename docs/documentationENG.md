EN:

# Official Bullsploit Framework Documentation

All interaction with the bullsploit framework in the documentation takes place on an arch linux machine.

After installing the framework and starting the core following the short instructions from the README on the main page of the github repository, you will see a similar output to the console:

<img width="874" height="372" alt="image" src="https://github.com" />

This is the initial state of the framework and its main menu with an invitation to enter in bsc (bullsploit console). The menu displays a logo with a bull, where dev#1.1 is written near it, where 1.1 indicates the current version of the last release.
In order to start working with the framework, you need to find out what commands are available in this CLI application, to do this, enter the help command in bsc:

<img width="866" height="624" alt="image" src="https://github.com" />

As we can see, the following commands are available to us:

`help` - view available commands
    
`search` <moduletype> - search for a module by its type (payload/post/auxiliary/builder)

`usage` - view the terms of use and disclaimer via less

`github` - open the page with the official repository on github

`site` - open the website https://bullsploit.ru

`clear` - clear the terminal

`use <module path>` - use a module
    
`set <arguments>` - apply settings to the selected module
    
`run` - run the selected module
    
`exit` - terminate the bullsploit program process
    
`interact` - enter reverse shell mode with an available client
    
`options` - view available options for the selected module
    
`sessions` - view available sessions
    
`show` - view modified parameters for the current module
    
`back` - cancel selection

To start full-fledged work with the framework, you must first select the module you want to work with. To find a suitable module, enter the search command, which displays a table of all found modules according to the structure: number, name, creation date, rank, brief description.
<img width="948" height="354" alt="image" src="https://github.com" />

I will analyze the usage process using the pyasyncioscan module (Asynchronous python port scanner) as an example

To start working with it, you need to select it in the console with the use command:

<img width="948" height="354" alt="image" src="https://github.com" />

Now the console has an attribute with the name of the selected module, this signals that the console has found it, selected it and is ready to work with it.

Then we need to see what parameters the selected module requires with the options command:

<img width="600" height="171" alt="image" src="https://github.com" />

As we can see, for the asynchronous port scanner to work, you need to specify the ip and port range of the target device.

We will specify these parameters with the set command:

<img width="554" height="88" alt="image" src="https://github.com" />

As you can see, the parameters were successfully applied. Now the module has the data necessary for operation passed to it as parameters and it is ready to work. Let's run it with the run command:

<img width="556" height="111" alt="image" src="https://github.com" />

It worked successfully and quickly gave us open ports.
