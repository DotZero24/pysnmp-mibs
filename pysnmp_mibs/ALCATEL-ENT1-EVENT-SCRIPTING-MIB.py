_R='eventActionGroup'
_Q='eventActionGlobalsGroup'
_P='alaEventActionRowStatus'
_O='alaEventActionScriptLaunchCount'
_N='alaEventActionScriptLastLaunched'
_M='alaEventActionScriptLastChanged'
_L='alaEventActionScriptPath'
_K='alaEventActionGlobalScriptTimeLimit'
_J='read-create'
_I='not-accessible'
_H='alaEventActionName'
_G='alaEventActionType'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='SnmpAdminString'
_B='ALCATEL-ENT1-EVENT-SCRIPTING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1EventScripting,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1EventScripting')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1EventScriptingMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1))
_AlcatelIND1EventScriptingObjects_ObjectIdentity=ObjectIdentity
alcatelIND1EventScriptingObjects=_AlcatelIND1EventScriptingObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1,1))
if mibBuilder.loadTexts:alcatelIND1EventScriptingObjects.setStatus(_A)
_AlaEventActionGlobalConfigObjects_ObjectIdentity=ObjectIdentity
alaEventActionGlobalConfigObjects=_AlaEventActionGlobalConfigObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1))
class _AlaEventActionGlobalScriptTimeLimit_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_AlaEventActionGlobalScriptTimeLimit_Type.__name__=_F
_AlaEventActionGlobalScriptTimeLimit_Object=MibScalar
alaEventActionGlobalScriptTimeLimit=_AlaEventActionGlobalScriptTimeLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,1),_AlaEventActionGlobalScriptTimeLimit_Type())
alaEventActionGlobalScriptTimeLimit.setMaxAccess('read-write')
if mibBuilder.loadTexts:alaEventActionGlobalScriptTimeLimit.setStatus(_A)
_AlaEventActionTable_Object=MibTable
alaEventActionTable=_AlaEventActionTable_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2))
if mibBuilder.loadTexts:alaEventActionTable.setStatus(_A)
_AlaEventActionEntry_Object=MibTableRow
alaEventActionEntry=_AlaEventActionEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1))
alaEventActionEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:alaEventActionEntry.setStatus(_A)
class _AlaEventActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('trap',1))
_AlaEventActionType_Type.__name__=_E
_AlaEventActionType_Object=MibTableColumn
alaEventActionType=_AlaEventActionType_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,1),_AlaEventActionType_Type())
alaEventActionType.setMaxAccess(_I)
if mibBuilder.loadTexts:alaEventActionType.setStatus(_A)
class _AlaEventActionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AlaEventActionName_Type.__name__=_C
_AlaEventActionName_Object=MibTableColumn
alaEventActionName=_AlaEventActionName_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,2),_AlaEventActionName_Type())
alaEventActionName.setMaxAccess(_I)
if mibBuilder.loadTexts:alaEventActionName.setStatus(_A)
class _AlaEventActionScriptPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AlaEventActionScriptPath_Type.__name__=_C
_AlaEventActionScriptPath_Object=MibTableColumn
alaEventActionScriptPath=_AlaEventActionScriptPath_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,3),_AlaEventActionScriptPath_Type())
alaEventActionScriptPath.setMaxAccess(_J)
if mibBuilder.loadTexts:alaEventActionScriptPath.setStatus(_A)
_AlaEventActionScriptLastChanged_Type=DateAndTime
_AlaEventActionScriptLastChanged_Object=MibTableColumn
alaEventActionScriptLastChanged=_AlaEventActionScriptLastChanged_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,4),_AlaEventActionScriptLastChanged_Type())
alaEventActionScriptLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:alaEventActionScriptLastChanged.setStatus(_A)
_AlaEventActionScriptLastLaunched_Type=DateAndTime
_AlaEventActionScriptLastLaunched_Object=MibTableColumn
alaEventActionScriptLastLaunched=_AlaEventActionScriptLastLaunched_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,5),_AlaEventActionScriptLastLaunched_Type())
alaEventActionScriptLastLaunched.setMaxAccess(_D)
if mibBuilder.loadTexts:alaEventActionScriptLastLaunched.setStatus(_A)
_AlaEventActionScriptLaunchCount_Type=Counter32
_AlaEventActionScriptLaunchCount_Object=MibTableColumn
alaEventActionScriptLaunchCount=_AlaEventActionScriptLaunchCount_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,6),_AlaEventActionScriptLaunchCount_Type())
alaEventActionScriptLaunchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaEventActionScriptLaunchCount.setStatus(_A)
_AlaEventActionRowStatus_Type=RowStatus
_AlaEventActionRowStatus_Object=MibTableColumn
alaEventActionRowStatus=_AlaEventActionRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,86,1,1,1,2,1,7),_AlaEventActionRowStatus_Type())
alaEventActionRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:alaEventActionRowStatus.setStatus(_A)
_AlcatelIND1EventScriptingMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1EventScriptingMIBConformance=_AlcatelIND1EventScriptingMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1,2))
if mibBuilder.loadTexts:alcatelIND1EventScriptingMIBConformance.setStatus(_A)
_AlcatelIND1EventScriptingMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1EventScriptingMIBGroups=_AlcatelIND1EventScriptingMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1,2,1))
if mibBuilder.loadTexts:alcatelIND1EventScriptingMIBGroups.setStatus(_A)
_AlcatelIND1EventScriptingMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1EventScriptingMIBCompliances=_AlcatelIND1EventScriptingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86,1,2,2))
if mibBuilder.loadTexts:alcatelIND1EventScriptingMIBCompliances.setStatus(_A)
eventActionGlobalsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,86,1,2,1,1))
eventActionGlobalsGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:eventActionGlobalsGroup.setStatus(_A)
eventActionGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,86,1,2,1,2))
eventActionGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:eventActionGroup.setStatus(_A)
alcatelIND1EventScriptingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,86,1,2,2,1))
alcatelIND1EventScriptingMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:alcatelIND1EventScriptingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1EventScriptingMIB':alcatelIND1EventScriptingMIB,'alcatelIND1EventScriptingObjects':alcatelIND1EventScriptingObjects,'alaEventActionGlobalConfigObjects':alaEventActionGlobalConfigObjects,_K:alaEventActionGlobalScriptTimeLimit,'alaEventActionTable':alaEventActionTable,'alaEventActionEntry':alaEventActionEntry,_G:alaEventActionType,_H:alaEventActionName,_L:alaEventActionScriptPath,_M:alaEventActionScriptLastChanged,_N:alaEventActionScriptLastLaunched,_O:alaEventActionScriptLaunchCount,_P:alaEventActionRowStatus,'alcatelIND1EventScriptingMIBConformance':alcatelIND1EventScriptingMIBConformance,'alcatelIND1EventScriptingMIBGroups':alcatelIND1EventScriptingMIBGroups,_Q:eventActionGlobalsGroup,_R:eventActionGroup,'alcatelIND1EventScriptingMIBCompliances':alcatelIND1EventScriptingMIBCompliances,'alcatelIND1EventScriptingMIBCompliance':alcatelIND1EventScriptingMIBCompliance})