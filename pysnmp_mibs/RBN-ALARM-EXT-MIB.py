_X='rbnAlarmClearGroup'
_W='rbnAlarmModelGroup'
_V='rbnAlarmClearResourceCounter64Val'
_U='rbnAlarmClearResourceOidVal'
_T='rbnAlarmClearResourceIpAddressVal'
_S='rbnAlarmClearResourceOctetStringVal'
_R='rbnAlarmClearResourceInteger32Val'
_Q='rbnAlarmClearResourceTimeTicksVal'
_P='rbnAlarmClearResourceUnsigned32Val'
_O='rbnAlarmClearResourceCounter32Val'
_N='rbnAlarmClearResourceValueType'
_M='rbnAlarmClearResourceID'
_L='rbnAlarmModelResourceIdx'
_K='rbnAlarmModelEntry'
_J='Unsigned32'
_I='Integer32'
_H='alarmListName'
_G='alarmClearIndex'
_F='alarmClearDateAndTime'
_E='OctetString'
_D='ALARM-MIB'
_C='read-only'
_B='RBN-ALARM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmClearDateAndTime,alarmClearIndex,alarmListName,alarmModelEntry=mibBuilder.importSymbols(_D,_F,_G,_H,'alarmModelEntry')
rbnModules,=mibBuilder.importSymbols('RBN-SMI','rbnModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnAlarmExtMib=ModuleIdentity((1,3,6,1,4,1,2352,5,53))
if mibBuilder.loadTexts:rbnAlarmExtMib.setRevisions(('2009-09-18 18:00',))
_RbnAlarmObjects_ObjectIdentity=ObjectIdentity
rbnAlarmObjects=_RbnAlarmObjects_ObjectIdentity((1,3,6,1,4,1,2352,5,53,1))
_RbnAlarmModel_ObjectIdentity=ObjectIdentity
rbnAlarmModel=_RbnAlarmModel_ObjectIdentity((1,3,6,1,4,1,2352,5,53,1,1))
_RbnAlarmModelTable_Object=MibTable
rbnAlarmModelTable=_RbnAlarmModelTable_Object((1,3,6,1,4,1,2352,5,53,1,1,1))
if mibBuilder.loadTexts:rbnAlarmModelTable.setStatus(_A)
_RbnAlarmModelEntry_Object=MibTableRow
rbnAlarmModelEntry=_RbnAlarmModelEntry_Object((1,3,6,1,4,1,2352,5,53,1,1,1,1))
if mibBuilder.loadTexts:rbnAlarmModelEntry.setStatus(_A)
class _RbnAlarmModelResourceIdx_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,512))
_RbnAlarmModelResourceIdx_Type.__name__=_J
_RbnAlarmModelResourceIdx_Object=MibTableColumn
rbnAlarmModelResourceIdx=_RbnAlarmModelResourceIdx_Object((1,3,6,1,4,1,2352,5,53,1,1,1,1,1),_RbnAlarmModelResourceIdx_Type())
rbnAlarmModelResourceIdx.setMaxAccess('read-create')
if mibBuilder.loadTexts:rbnAlarmModelResourceIdx.setStatus(_A)
_RbnAlarmActive_ObjectIdentity=ObjectIdentity
rbnAlarmActive=_RbnAlarmActive_ObjectIdentity((1,3,6,1,4,1,2352,5,53,1,2))
_RbnAlarmClear_ObjectIdentity=ObjectIdentity
rbnAlarmClear=_RbnAlarmClear_ObjectIdentity((1,3,6,1,4,1,2352,5,53,1,3))
_RbnAlarmClearResourceTable_Object=MibTable
rbnAlarmClearResourceTable=_RbnAlarmClearResourceTable_Object((1,3,6,1,4,1,2352,5,53,1,3,1))
if mibBuilder.loadTexts:rbnAlarmClearResourceTable.setStatus(_A)
_RbnAlarmClearResourceEntry_Object=MibTableRow
rbnAlarmClearResourceEntry=_RbnAlarmClearResourceEntry_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1))
rbnAlarmClearResourceEntry.setIndexNames((0,_D,_H),(0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:rbnAlarmClearResourceEntry.setStatus(_A)
_RbnAlarmClearResourceID_Type=ObjectIdentifier
_RbnAlarmClearResourceID_Object=MibTableColumn
rbnAlarmClearResourceID=_RbnAlarmClearResourceID_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,1),_RbnAlarmClearResourceID_Type())
rbnAlarmClearResourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceID.setStatus(_A)
class _RbnAlarmClearResourceValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('counter32',1),('unsigned32',2),('timeTicks',3),('integer32',4),('ipAddress',5),('octetString',6),('objectId',7),('counter64',8)))
_RbnAlarmClearResourceValueType_Type.__name__=_I
_RbnAlarmClearResourceValueType_Object=MibTableColumn
rbnAlarmClearResourceValueType=_RbnAlarmClearResourceValueType_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,3),_RbnAlarmClearResourceValueType_Type())
rbnAlarmClearResourceValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceValueType.setStatus(_A)
_RbnAlarmClearResourceCounter32Val_Type=Counter32
_RbnAlarmClearResourceCounter32Val_Object=MibTableColumn
rbnAlarmClearResourceCounter32Val=_RbnAlarmClearResourceCounter32Val_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,4),_RbnAlarmClearResourceCounter32Val_Type())
rbnAlarmClearResourceCounter32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceCounter32Val.setStatus(_A)
_RbnAlarmClearResourceUnsigned32Val_Type=Unsigned32
_RbnAlarmClearResourceUnsigned32Val_Object=MibTableColumn
rbnAlarmClearResourceUnsigned32Val=_RbnAlarmClearResourceUnsigned32Val_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,5),_RbnAlarmClearResourceUnsigned32Val_Type())
rbnAlarmClearResourceUnsigned32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceUnsigned32Val.setStatus(_A)
_RbnAlarmClearResourceTimeTicksVal_Type=TimeTicks
_RbnAlarmClearResourceTimeTicksVal_Object=MibTableColumn
rbnAlarmClearResourceTimeTicksVal=_RbnAlarmClearResourceTimeTicksVal_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,6),_RbnAlarmClearResourceTimeTicksVal_Type())
rbnAlarmClearResourceTimeTicksVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceTimeTicksVal.setStatus(_A)
_RbnAlarmClearResourceInteger32Val_Type=Integer32
_RbnAlarmClearResourceInteger32Val_Object=MibTableColumn
rbnAlarmClearResourceInteger32Val=_RbnAlarmClearResourceInteger32Val_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,7),_RbnAlarmClearResourceInteger32Val_Type())
rbnAlarmClearResourceInteger32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceInteger32Val.setStatus(_A)
class _RbnAlarmClearResourceOctetStringVal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_RbnAlarmClearResourceOctetStringVal_Type.__name__=_E
_RbnAlarmClearResourceOctetStringVal_Object=MibTableColumn
rbnAlarmClearResourceOctetStringVal=_RbnAlarmClearResourceOctetStringVal_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,8),_RbnAlarmClearResourceOctetStringVal_Type())
rbnAlarmClearResourceOctetStringVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceOctetStringVal.setStatus(_A)
_RbnAlarmClearResourceIpAddressVal_Type=IpAddress
_RbnAlarmClearResourceIpAddressVal_Object=MibTableColumn
rbnAlarmClearResourceIpAddressVal=_RbnAlarmClearResourceIpAddressVal_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,9),_RbnAlarmClearResourceIpAddressVal_Type())
rbnAlarmClearResourceIpAddressVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceIpAddressVal.setStatus(_A)
_RbnAlarmClearResourceOidVal_Type=ObjectIdentifier
_RbnAlarmClearResourceOidVal_Object=MibTableColumn
rbnAlarmClearResourceOidVal=_RbnAlarmClearResourceOidVal_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,10),_RbnAlarmClearResourceOidVal_Type())
rbnAlarmClearResourceOidVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceOidVal.setStatus(_A)
_RbnAlarmClearResourceCounter64Val_Type=Counter64
_RbnAlarmClearResourceCounter64Val_Object=MibTableColumn
rbnAlarmClearResourceCounter64Val=_RbnAlarmClearResourceCounter64Val_Object((1,3,6,1,4,1,2352,5,53,1,3,1,1,11),_RbnAlarmClearResourceCounter64Val_Type())
rbnAlarmClearResourceCounter64Val.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAlarmClearResourceCounter64Val.setStatus(_A)
_RbnAlarmExtConformance_ObjectIdentity=ObjectIdentity
rbnAlarmExtConformance=_RbnAlarmExtConformance_ObjectIdentity((1,3,6,1,4,1,2352,5,53,2))
_RbnAlarmExtCompliances_ObjectIdentity=ObjectIdentity
rbnAlarmExtCompliances=_RbnAlarmExtCompliances_ObjectIdentity((1,3,6,1,4,1,2352,5,53,2,1))
_RbnAlarmExtGroups_ObjectIdentity=ObjectIdentity
rbnAlarmExtGroups=_RbnAlarmExtGroups_ObjectIdentity((1,3,6,1,4,1,2352,5,53,2,2))
alarmModelEntry.registerAugmentions((_B,_K))
rbnAlarmModelEntry.setIndexNames(*alarmModelEntry.getIndexNames())
rbnAlarmModelGroup=ObjectGroup((1,3,6,1,4,1,2352,5,53,2,2,1))
rbnAlarmModelGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:rbnAlarmModelGroup.setStatus(_A)
rbnAlarmClearGroup=ObjectGroup((1,3,6,1,4,1,2352,5,53,2,2,2))
rbnAlarmClearGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:rbnAlarmClearGroup.setStatus(_A)
rbnAlarmExtCompliance=ModuleCompliance((1,3,6,1,4,1,2352,5,53,2,1,1))
rbnAlarmExtCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:rbnAlarmExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnAlarmExtMib':rbnAlarmExtMib,'rbnAlarmObjects':rbnAlarmObjects,'rbnAlarmModel':rbnAlarmModel,'rbnAlarmModelTable':rbnAlarmModelTable,_K:rbnAlarmModelEntry,_L:rbnAlarmModelResourceIdx,'rbnAlarmActive':rbnAlarmActive,'rbnAlarmClear':rbnAlarmClear,'rbnAlarmClearResourceTable':rbnAlarmClearResourceTable,'rbnAlarmClearResourceEntry':rbnAlarmClearResourceEntry,_M:rbnAlarmClearResourceID,_N:rbnAlarmClearResourceValueType,_O:rbnAlarmClearResourceCounter32Val,_P:rbnAlarmClearResourceUnsigned32Val,_Q:rbnAlarmClearResourceTimeTicksVal,_R:rbnAlarmClearResourceInteger32Val,_S:rbnAlarmClearResourceOctetStringVal,_T:rbnAlarmClearResourceIpAddressVal,_U:rbnAlarmClearResourceOidVal,_V:rbnAlarmClearResourceCounter64Val,'rbnAlarmExtConformance':rbnAlarmExtConformance,'rbnAlarmExtCompliances':rbnAlarmExtCompliances,'rbnAlarmExtCompliance':rbnAlarmExtCompliance,'rbnAlarmExtGroups':rbnAlarmExtGroups,_W:rbnAlarmModelGroup,_X:rbnAlarmClearGroup})