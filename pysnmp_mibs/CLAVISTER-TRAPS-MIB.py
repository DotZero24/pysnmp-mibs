_N='clavisterOSTrapGroupVar'
_M='clavisterOSTrapGroupTrap'
_L='clavisterOSGenericTrap'
_K='Integer32'
_J='clavisterOSTrapVarMessage'
_I='clavisterOSTrapVarTime'
_H='clavisterOSTrapVarAction'
_G='clavisterOSTrapVarEvent'
_F='clavisterOSTrapVarID'
_E='clavisterOSTrapVarCategory'
_D='clavisterOSTrapVarSeverity'
_C='accessible-for-notify'
_B='current'
_A='CLAVISTER-TRAPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clavisterOSTrap,clavisterOSTrapInfo=mibBuilder.importSymbols('CLAVISTER-SMI','clavisterOSTrap','clavisterOSTrapInfo')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
clavisterOSTrapMibModule=ModuleIdentity((1,3,6,1,4,1,5089,1,1,0))
if mibBuilder.loadTexts:clavisterOSTrapMibModule.setRevisions(('2015-10-21 17:00','2007-10-31 00:00'))
class _ClavisterOSTrapVarSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_ClavisterOSTrapVarSeverity_Type.__name__=_K
_ClavisterOSTrapVarSeverity_Object=MibScalar
clavisterOSTrapVarSeverity=_ClavisterOSTrapVarSeverity_Object((1,3,6,1,4,1,5089,1,1,4),_ClavisterOSTrapVarSeverity_Type())
clavisterOSTrapVarSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarSeverity.setStatus(_B)
_ClavisterOSTrapVarCategory_Type=DisplayString
_ClavisterOSTrapVarCategory_Object=MibScalar
clavisterOSTrapVarCategory=_ClavisterOSTrapVarCategory_Object((1,3,6,1,4,1,5089,1,1,5),_ClavisterOSTrapVarCategory_Type())
clavisterOSTrapVarCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarCategory.setStatus(_B)
_ClavisterOSTrapVarID_Type=DisplayString
_ClavisterOSTrapVarID_Object=MibScalar
clavisterOSTrapVarID=_ClavisterOSTrapVarID_Object((1,3,6,1,4,1,5089,1,1,6),_ClavisterOSTrapVarID_Type())
clavisterOSTrapVarID.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarID.setStatus(_B)
_ClavisterOSTrapVarEvent_Type=DisplayString
_ClavisterOSTrapVarEvent_Object=MibScalar
clavisterOSTrapVarEvent=_ClavisterOSTrapVarEvent_Object((1,3,6,1,4,1,5089,1,1,7),_ClavisterOSTrapVarEvent_Type())
clavisterOSTrapVarEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarEvent.setStatus(_B)
_ClavisterOSTrapVarAction_Type=DisplayString
_ClavisterOSTrapVarAction_Object=MibScalar
clavisterOSTrapVarAction=_ClavisterOSTrapVarAction_Object((1,3,6,1,4,1,5089,1,1,8),_ClavisterOSTrapVarAction_Type())
clavisterOSTrapVarAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarAction.setStatus(_B)
_ClavisterOSTrapVarTime_Type=DisplayString
_ClavisterOSTrapVarTime_Object=MibScalar
clavisterOSTrapVarTime=_ClavisterOSTrapVarTime_Object((1,3,6,1,4,1,5089,1,1,9),_ClavisterOSTrapVarTime_Type())
clavisterOSTrapVarTime.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarTime.setStatus(_B)
_ClavisterOSTrapVarMessage_Type=DisplayString
_ClavisterOSTrapVarMessage_Object=MibScalar
clavisterOSTrapVarMessage=_ClavisterOSTrapVarMessage_Object((1,3,6,1,4,1,5089,1,1,10),_ClavisterOSTrapVarMessage_Type())
clavisterOSTrapVarMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:clavisterOSTrapVarMessage.setStatus(_B)
clavisterOSTrapGroupVar=ObjectGroup((1,3,6,1,4,1,5089,1,1,2))
clavisterOSTrapGroupVar.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:clavisterOSTrapGroupVar.setStatus(_B)
clavisterOSGenericTrap=NotificationType((1,3,6,1,4,1,5089,1,0,1))
clavisterOSGenericTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:clavisterOSGenericTrap.setStatus(_B)
clavisterOSTrapGroupTrap=NotificationGroup((1,3,6,1,4,1,5089,1,1,1))
clavisterOSTrapGroupTrap.setObjects((_A,_L))
if mibBuilder.loadTexts:clavisterOSTrapGroupTrap.setStatus(_B)
clavisterOSTrapCompliance=ModuleCompliance((1,3,6,1,4,1,5089,1,1,3))
clavisterOSTrapCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:clavisterOSTrapCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_L:clavisterOSGenericTrap,'clavisterOSTrapMibModule':clavisterOSTrapMibModule,_M:clavisterOSTrapGroupTrap,_N:clavisterOSTrapGroupVar,'clavisterOSTrapCompliance':clavisterOSTrapCompliance,_D:clavisterOSTrapVarSeverity,_E:clavisterOSTrapVarCategory,_F:clavisterOSTrapVarID,_G:clavisterOSTrapVarEvent,_H:clavisterOSTrapVarAction,_I:clavisterOSTrapVarTime,_J:clavisterOSTrapVarMessage})