
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x9b\xbdm\xc5;8O\xfa=\xdd\xa8\x9e\x88\x1f%\x8a'
    
_lr_action_items = {'SYNCHRONIZATION':([24,40,41,61,63,79,87,],[39,-36,-1,-33,-34,-1,-35,]),'$end':([0,1,4,5,6,7,12,32,33,36,37,],[-1,-1,0,-1,-55,-53,-54,-49,-52,-50,-51,]),'FLECHE':([88,89,],[95,-25,]),'TRANSITION':([26,44,45,70,72,82,90,],[42,-32,-1,-31,-38,-1,-39,]),'STATE':([8,9,10,11,],[15,-4,-3,15,]),'POINT':([86,],[94,]),'OBSERVER':([38,39,42,43,55,56,59,60,64,67,68,77,81,85,91,93,96,97,98,99,100,],[52,-1,-1,52,-1,-10,-13,-11,-30,-28,-1,-12,-29,-1,-8,-6,-1,-5,-24,-26,-7,]),'VIRGULE':([28,29,30,31,40,41,44,45,73,74,79,82,],[-23,46,49,-15,-36,62,-32,71,46,49,62,71,]),'BLOCK':([0,1,5,8,9,10,11,20,21,30,31,32,33,36,37,50,51,74,84,],[2,2,2,2,-4,-3,2,2,2,-1,-15,-49,-52,-50,-51,-16,-18,-1,-17,]),'CLASS':([0,1,5,32,33,36,37,],[3,3,3,-49,-52,-50,-51,]),'ANDCOMMERCIAL':([85,96,97,],[92,92,-5,]),'IDENTIFIER':([2,3,8,9,10,11,15,16,17,20,21,25,27,30,31,32,33,39,42,46,49,50,51,55,56,62,68,71,74,78,80,84,85,91,92,93,94,95,96,97,98,99,100,],[9,10,17,-4,-3,17,28,31,-14,17,17,40,44,-1,-15,-49,-52,58,66,28,31,-16,-18,58,-10,40,66,44,-1,86,89,-17,-1,-8,86,-6,97,99,-1,-5,-24,-26,-7,]),'DEUXPOINTS':([57,58,65,66,],[78,-9,80,-27,]),'EVENT':([13,14,20,21,28,29,30,31,32,33,34,35,47,48,50,51,73,74,83,84,],[25,27,-19,-20,-23,-1,-1,-15,-49,-52,-21,-22,-40,-37,-16,-18,-1,-1,-41,-17,]),'END':([18,19,22,23,38,39,42,43,52,53,54,55,56,59,60,64,67,68,69,75,76,77,81,85,91,93,96,97,98,99,100,],[32,-47,-48,36,-1,-1,-1,-1,-1,-43,-45,-1,-10,-13,-11,-30,-28,-1,-46,-44,-42,-12,-29,-1,-8,-6,-1,-5,-24,-26,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ClassInstanceIdentifier':([16,49,],[30,74,]),'ComposedBlockClause':([8,11,20,21,],[13,13,34,35,]),'Class':([0,1,5,],[5,5,5,]),'Model':([0,1,5,],[4,7,12,]),'AndCommercialEvenPathStar':([85,96,],[91,100,]),'StateClause':([8,11,],[14,14,]),'EndClass':([23,],[37,]),'OriginalStateIdentifierInTransition':([80,],[88,]),'ClassInstanceVirguleIdentifierStar':([30,74,],[51,84,]),'EventClauseInBlock':([13,],[24,]),'Synchronization':([39,55,],[55,55,]),'DestStateIdentifierInTransition':([95,],[98,]),'ClassNameIdentifier':([8,11,20,21,],[16,16,16,16,]),'InternalBlockBody':([8,11,],[22,22,]),'StateVirguleIdentifierStar':([29,73,],[48,83,]),'EventVirguleIdentifierStarInBlock':([41,79,],[61,87,]),'ClassIdentifier':([3,],[11,]),'ObserverClauseQuestionMark':([38,43,],[54,69,]),'EventPath':([78,92,],[85,96,]),'BlockBody':([8,11,],[18,23,]),'BlockIdentifier':([2,],[8,]),'SynchronizationClause':([24,],[38,]),'SynchronizationStar':([39,55,],[59,77,]),'Block':([0,1,5,8,11,20,21,],[1,1,1,20,20,20,20,]),'StateIdentifier':([15,46,],[29,73,]),'EventIdentifierInTransition':([42,68,],[65,65,]),'BasicBlockBody':([8,11,],[19,19,]),'TransitionClause':([26,],[43,]),'ObserverStar':([52,],[75,]),'MacroEventDefinition':([39,55,],[56,56,]),'EventClauseInClass':([14,],[26,]),'EventIdentifierInBlock':([25,62,],[41,79,]),'EndBlock':([18,],[33,]),'EventVirguleIdentifierStarInClass':([45,82,],[70,90,]),'ClassInstance':([8,11,20,21,],[21,21,21,21,]),'EventIdentifierInSynchronization':([39,55,],[57,57,]),'Transition':([42,68,],[68,68,]),'empty':([0,1,5,29,30,38,39,41,42,43,45,52,55,68,73,74,79,82,85,96,],[6,6,6,47,50,53,60,63,67,53,72,76,60,67,47,50,63,72,93,93,]),'EventIdentifierInClass':([27,71,],[45,82,]),'TransitionStar':([42,68,],[64,81,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Model","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',30),
  ('Identifier -> IDENTIFIER','Identifier',1,'p_Identifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',34),
  ('ClassIdentifier -> IDENTIFIER','ClassIdentifier',1,'p_ClassIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',37),
  ('BlockIdentifier -> IDENTIFIER','BlockIdentifier',1,'p_BlockIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',41),
  ('EventPath -> IDENTIFIER POINT IDENTIFIER','EventPath',3,'p_EventPath','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',59),
  ('AndCommercialEvenPathStar -> empty','AndCommercialEvenPathStar',1,'p_AndCommercialEvenPathStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',78),
  ('AndCommercialEvenPathStar -> ANDCOMMERCIAL EventPath AndCommercialEvenPathStar','AndCommercialEvenPathStar',3,'p_AndCommercialEvenPathStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',79),
  ('MacroEventDefinition -> EventIdentifierInSynchronization DEUXPOINTS EventPath AndCommercialEvenPathStar','MacroEventDefinition',4,'p_MacroEventDefinition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',82),
  ('EventIdentifierInSynchronization -> IDENTIFIER','EventIdentifierInSynchronization',1,'p_EventIdentifierInSynchronization','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',91),
  ('Synchronization -> MacroEventDefinition','Synchronization',1,'p_Synchronization','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',95),
  ('SynchronizationStar -> empty','SynchronizationStar',1,'p_SynchronizationStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',98),
  ('SynchronizationStar -> Synchronization SynchronizationStar','SynchronizationStar',2,'p_SynchronizationStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',99),
  ('SynchronizationClause -> SYNCHRONIZATION SynchronizationStar','SynchronizationClause',2,'p_SynchronizationClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',102),
  ('ClassNameIdentifier -> IDENTIFIER','ClassNameIdentifier',1,'p_ClassNameIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',105),
  ('ClassInstanceIdentifier -> IDENTIFIER','ClassInstanceIdentifier',1,'p_ClassInstanceIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',109),
  ('ClassInstanceVirguleIdentifierStar -> empty','ClassInstanceVirguleIdentifierStar',1,'p_ClassInstanceVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',113),
  ('ClassInstanceVirguleIdentifierStar -> VIRGULE ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar','ClassInstanceVirguleIdentifierStar',3,'p_ClassInstanceVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',114),
  ('ClassInstance -> ClassNameIdentifier ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar','ClassInstance',3,'p_ClassInstance','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',118),
  ('ComposedBlockClause -> Block','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',121),
  ('ComposedBlockClause -> ClassInstance','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',122),
  ('ComposedBlockClause -> Block ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',123),
  ('ComposedBlockClause -> ClassInstance ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',124),
  ('StateIdentifier -> IDENTIFIER','StateIdentifier',1,'p_StateIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',132),
  ('Transition -> EventIdentifierInTransition DEUXPOINTS OriginalStateIdentifierInTransition FLECHE DestStateIdentifierInTransition','Transition',5,'p_Transition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',140),
  ('OriginalStateIdentifierInTransition -> IDENTIFIER','OriginalStateIdentifierInTransition',1,'p_OriginalStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',143),
  ('DestStateIdentifierInTransition -> IDENTIFIER','DestStateIdentifierInTransition',1,'p_DestStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',147),
  ('EventIdentifierInTransition -> IDENTIFIER','EventIdentifierInTransition',1,'p_EventIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',151),
  ('TransitionStar -> empty','TransitionStar',1,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',155),
  ('TransitionStar -> Transition TransitionStar','TransitionStar',2,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',156),
  ('TransitionClause -> TRANSITION TransitionStar','TransitionClause',2,'p_TransitionClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',159),
  ('EventClauseInClass -> EVENT EventIdentifierInClass EventVirguleIdentifierStarInClass','EventClauseInClass',3,'p_EventClauseInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',162),
  ('EventIdentifierInClass -> IDENTIFIER','EventIdentifierInClass',1,'p_EventIdentifierInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',165),
  ('EventClauseInBlock -> EVENT EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventClauseInBlock',3,'p_EventClauseInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',169),
  ('EventVirguleIdentifierStarInBlock -> empty','EventVirguleIdentifierStarInBlock',1,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',172),
  ('EventVirguleIdentifierStarInBlock -> VIRGULE EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventVirguleIdentifierStarInBlock',3,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',173),
  ('EventIdentifierInBlock -> IDENTIFIER','EventIdentifierInBlock',1,'p_EventIdentifierInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',176),
  ('StateClause -> STATE StateIdentifier StateVirguleIdentifierStar','StateClause',3,'p_StateClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',180),
  ('EventVirguleIdentifierStarInClass -> empty','EventVirguleIdentifierStarInClass',1,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',183),
  ('EventVirguleIdentifierStarInClass -> VIRGULE EventIdentifierInClass EventVirguleIdentifierStarInClass','EventVirguleIdentifierStarInClass',3,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',184),
  ('StateVirguleIdentifierStar -> empty','StateVirguleIdentifierStar',1,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',187),
  ('StateVirguleIdentifierStar -> VIRGULE StateIdentifier StateVirguleIdentifierStar','StateVirguleIdentifierStar',3,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',188),
  ('ObserverStar -> empty','ObserverStar',1,'p_ObserverStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',191),
  ('ObserverClauseQuestionMark -> empty','ObserverClauseQuestionMark',1,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',195),
  ('ObserverClauseQuestionMark -> OBSERVER ObserverStar','ObserverClauseQuestionMark',2,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',196),
  ('InternalBlockBody -> ComposedBlockClause EventClauseInBlock SynchronizationClause ObserverClauseQuestionMark','InternalBlockBody',4,'p_InternalBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',199),
  ('BasicBlockBody -> StateClause EventClauseInClass TransitionClause ObserverClauseQuestionMark','BasicBlockBody',4,'p_BasicBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',203),
  ('BlockBody -> BasicBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',207),
  ('BlockBody -> InternalBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',208),
  ('EndBlock -> END','EndBlock',1,'p_EndBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',212),
  ('EndClass -> END','EndClass',1,'p_EndClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',226),
  ('Class -> CLASS ClassIdentifier BlockBody EndClass','Class',4,'p_Class','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',250),
  ('Block -> BLOCK BlockIdentifier BlockBody EndBlock','Block',4,'p_Block','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',254),
  ('Model -> Block Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',257),
  ('Model -> Class Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',258),
  ('Model -> empty','Model',1,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',259),
]