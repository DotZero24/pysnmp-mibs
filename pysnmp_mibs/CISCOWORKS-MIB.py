_P='ciscoCwNotificationsGroup'
_O='ciscoCwObjectsGroup'
_N='cwDevLogTrap'
_M='cwAppLogTrap'
_L='Integer32'
_K='ciscoworks'
_J='cwLogApp'
_I='sysUpTime'
_H='SNMPv2-MIB'
_G='cwLogMsg'
_F='cwLogSource'
_E='cwLogDate'
_D='read-only'
_C='DisplayString'
_B='current'
_A='CISCOWORKS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoworks,=mibBuilder.importSymbols('CISCO-SMI',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysUpTime,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
cwLogMIB=ModuleIdentity((1,3,6,1,4,1,9,14,1))
if mibBuilder.loadTexts:cwLogMIB.setRevisions(('2003-02-18 00:00','1995-04-02 00:00'))
_CwLog_ObjectIdentity=ObjectIdentity
cwLog=_CwLog_ObjectIdentity((1,3,6,1,4,1,9,14,1,1))
class _CwLogDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,15));fixedLength=15
_CwLogDate_Type.__name__=_C
_CwLogDate_Object=MibScalar
cwLogDate=_CwLogDate_Object((1,3,6,1,4,1,9,14,1,1,1),_CwLogDate_Type())
cwLogDate.setMaxAccess(_D)
if mibBuilder.loadTexts:cwLogDate.setStatus(_B)
class _CwLogSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_K,2),('device',3)))
_CwLogSource_Type.__name__=_L
_CwLogSource_Object=MibScalar
cwLogSource=_CwLogSource_Object((1,3,6,1,4,1,9,14,1,1,2),_CwLogSource_Type())
cwLogSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cwLogSource.setStatus(_B)
class _CwLogApp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CwLogApp_Type.__name__=_C
_CwLogApp_Object=MibScalar
cwLogApp=_CwLogApp_Object((1,3,6,1,4,1,9,14,1,1,3),_CwLogApp_Type())
cwLogApp.setMaxAccess(_D)
if mibBuilder.loadTexts:cwLogApp.setStatus(_B)
class _CwLogMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CwLogMsg_Type.__name__=_C
_CwLogMsg_Object=MibScalar
cwLogMsg=_CwLogMsg_Object((1,3,6,1,4,1,9,14,1,1,4),_CwLogMsg_Type())
cwLogMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:cwLogMsg.setStatus(_B)
_CwTrapsPrefix_ObjectIdentity=ObjectIdentity
cwTrapsPrefix=_CwTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,9,14,1,2))
_CwTraps_ObjectIdentity=ObjectIdentity
cwTraps=_CwTraps_ObjectIdentity((1,3,6,1,4,1,9,14,1,2,0))
_CwMIBConform_ObjectIdentity=ObjectIdentity
cwMIBConform=_CwMIBConform_ObjectIdentity((1,3,6,1,4,1,9,14,1,3))
_CiscoCwMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCwMIBCompliances=_CiscoCwMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,14,1,3,1))
_CiscoCwMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCwMIBGroups=_CiscoCwMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,14,1,3,2))
ciscoCwObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,14,1,3,2,7))
ciscoCwObjectsGroup.setObjects(*((_A,_E),(_A,_F),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:ciscoCwObjectsGroup.setStatus(_B)
cwAppLogTrap=NotificationType((1,3,6,1,4,1,9,14,1,2,0,1))
cwAppLogTrap.setObjects(*((_H,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:cwAppLogTrap.setStatus(_B)
cwDevLogTrap=NotificationType((1,3,6,1,4,1,9,14,1,2,0,2))
cwDevLogTrap.setObjects(*((_H,_I),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cwDevLogTrap.setStatus(_B)
ciscoCwNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,14,1,3,2,12))
ciscoCwNotificationsGroup.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoCwNotificationsGroup.setStatus(_B)
ciscoCwMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,14,1,3,1,1))
ciscoCwMIBCompliance.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoCwMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cwLogMIB':cwLogMIB,'cwLog':cwLog,_E:cwLogDate,_F:cwLogSource,_J:cwLogApp,_G:cwLogMsg,'cwTrapsPrefix':cwTrapsPrefix,'cwTraps':cwTraps,_M:cwAppLogTrap,_N:cwDevLogTrap,'cwMIBConform':cwMIBConform,'ciscoCwMIBCompliances':ciscoCwMIBCompliances,'ciscoCwMIBCompliance':ciscoCwMIBCompliance,'ciscoCwMIBGroups':ciscoCwMIBGroups,_O:ciscoCwObjectsGroup,_P:ciscoCwNotificationsGroup})