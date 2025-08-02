_X='ciscoIetfD11QosExtNotifGroup'
_W='ciscoIetfD11QosExtNotifConGroup'
_V='ciscoIetfD11QosExtQueueGroup'
_U='ciscoIetfD11QosExtConfigGroup'
_T='ciscoIetfDot11QosExtChangeNotif'
_S='cid11QosExtNotifEnabled'
_R='cid11QosExtQueueQuota'
_Q='cid11QosExtVlanClassOfService'
_P='cid11QosExtOptionEnabled'
_O='cid11QosExtMaxRetry'
_N='cid11QosExtBackoffOffset'
_M='cid11QosExtVlanEntry'
_L='read-only'
_K='TruthValue'
_J='cid11TrafficPriority'
_I='Cid11QosTrafficCategory'
_H='read-write'
_G='cid11TrafficCategory'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='CISCO-IETF-DOT11-QOS-MIB'
_B='CISCO-IETF-DOT11-QOS-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Cid11QosTrafficCategory,cid11TrafficCategory,cid11TrafficPriority=mibBuilder.importSymbols(_C,_I,_G,_J)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
cwvlWlanVlanEntry,=mibBuilder.importSymbols('CISCO-WLAN-VLAN-MIB','cwvlWlanVlanEntry')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoIetfDot11QosExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,90))
if mibBuilder.loadTexts:ciscoIetfDot11QosExtMIB.setRevisions(('2002-04-01 00:00',))
_CiscoIetfDot11QosExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosExtMIBNotifs=_CiscoIetfDot11QosExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,90,0))
_CiscoIetfDot11QosExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosExtMIBObjects=_CiscoIetfDot11QosExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,90,1))
_Cid11QosExtConfig_ObjectIdentity=ObjectIdentity
cid11QosExtConfig=_Cid11QosExtConfig_ObjectIdentity((1,3,6,1,4,1,9,10,90,1,1))
_Cid11QosExtConfigTable_Object=MibTable
cid11QosExtConfigTable=_Cid11QosExtConfigTable_Object((1,3,6,1,4,1,9,10,90,1,1,1))
if mibBuilder.loadTexts:cid11QosExtConfigTable.setStatus(_A)
_Cid11QosExtConfigEntry_Object=MibTableRow
cid11QosExtConfigEntry=_Cid11QosExtConfigEntry_Object((1,3,6,1,4,1,9,10,90,1,1,1,1))
cid11QosExtConfigEntry.setIndexNames((0,_D,_E),(0,_C,_G))
if mibBuilder.loadTexts:cid11QosExtConfigEntry.setStatus(_A)
class _Cid11QosExtBackoffOffset_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Cid11QosExtBackoffOffset_Type.__name__=_F
_Cid11QosExtBackoffOffset_Object=MibTableColumn
cid11QosExtBackoffOffset=_Cid11QosExtBackoffOffset_Object((1,3,6,1,4,1,9,10,90,1,1,1,1,1),_Cid11QosExtBackoffOffset_Type())
cid11QosExtBackoffOffset.setMaxAccess(_H)
if mibBuilder.loadTexts:cid11QosExtBackoffOffset.setStatus(_A)
class _Cid11QosExtMaxRetry_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cid11QosExtMaxRetry_Type.__name__=_F
_Cid11QosExtMaxRetry_Object=MibTableColumn
cid11QosExtMaxRetry=_Cid11QosExtMaxRetry_Object((1,3,6,1,4,1,9,10,90,1,1,1,1,2),_Cid11QosExtMaxRetry_Type())
cid11QosExtMaxRetry.setMaxAccess(_H)
if mibBuilder.loadTexts:cid11QosExtMaxRetry.setStatus(_A)
_Cid11QosExtIfConfigTable_Object=MibTable
cid11QosExtIfConfigTable=_Cid11QosExtIfConfigTable_Object((1,3,6,1,4,1,9,10,90,1,1,2))
if mibBuilder.loadTexts:cid11QosExtIfConfigTable.setStatus(_A)
_Cid11QosExtIfConfigEntry_Object=MibTableRow
cid11QosExtIfConfigEntry=_Cid11QosExtIfConfigEntry_Object((1,3,6,1,4,1,9,10,90,1,1,2,1))
cid11QosExtIfConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cid11QosExtIfConfigEntry.setStatus(_A)
_Cid11QosExtOptionEnabled_Type=TruthValue
_Cid11QosExtOptionEnabled_Object=MibTableColumn
cid11QosExtOptionEnabled=_Cid11QosExtOptionEnabled_Object((1,3,6,1,4,1,9,10,90,1,1,2,1,1),_Cid11QosExtOptionEnabled_Type())
cid11QosExtOptionEnabled.setMaxAccess(_L)
if mibBuilder.loadTexts:cid11QosExtOptionEnabled.setStatus(_A)
_Cid11QosExtVlanTable_Object=MibTable
cid11QosExtVlanTable=_Cid11QosExtVlanTable_Object((1,3,6,1,4,1,9,10,90,1,1,3))
if mibBuilder.loadTexts:cid11QosExtVlanTable.setStatus(_A)
_Cid11QosExtVlanEntry_Object=MibTableRow
cid11QosExtVlanEntry=_Cid11QosExtVlanEntry_Object((1,3,6,1,4,1,9,10,90,1,1,3,1))
if mibBuilder.loadTexts:cid11QosExtVlanEntry.setStatus(_A)
class _Cid11QosExtVlanClassOfService_Type(Cid11QosTrafficCategory):defaultValue=0
_Cid11QosExtVlanClassOfService_Type.__name__=_I
_Cid11QosExtVlanClassOfService_Object=MibTableColumn
cid11QosExtVlanClassOfService=_Cid11QosExtVlanClassOfService_Object((1,3,6,1,4,1,9,10,90,1,1,3,1,1),_Cid11QosExtVlanClassOfService_Type())
cid11QosExtVlanClassOfService.setMaxAccess('read-create')
if mibBuilder.loadTexts:cid11QosExtVlanClassOfService.setStatus(_A)
_Cid11QosExtQueue_ObjectIdentity=ObjectIdentity
cid11QosExtQueue=_Cid11QosExtQueue_ObjectIdentity((1,3,6,1,4,1,9,10,90,1,2))
_Cid11QosExtQueueTable_Object=MibTable
cid11QosExtQueueTable=_Cid11QosExtQueueTable_Object((1,3,6,1,4,1,9,10,90,1,2,1))
if mibBuilder.loadTexts:cid11QosExtQueueTable.setStatus(_A)
_Cid11QosExtQueueEntry_Object=MibTableRow
cid11QosExtQueueEntry=_Cid11QosExtQueueEntry_Object((1,3,6,1,4,1,9,10,90,1,2,1,1))
cid11QosExtQueueEntry.setIndexNames((0,_D,_E),(0,_C,_G))
if mibBuilder.loadTexts:cid11QosExtQueueEntry.setStatus(_A)
class _Cid11QosExtQueueQuota_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Cid11QosExtQueueQuota_Type.__name__=_F
_Cid11QosExtQueueQuota_Object=MibTableColumn
cid11QosExtQueueQuota=_Cid11QosExtQueueQuota_Object((1,3,6,1,4,1,9,10,90,1,2,1,1,1),_Cid11QosExtQueueQuota_Type())
cid11QosExtQueueQuota.setMaxAccess(_L)
if mibBuilder.loadTexts:cid11QosExtQueueQuota.setStatus(_A)
_Cid11QosExtNotifControl_ObjectIdentity=ObjectIdentity
cid11QosExtNotifControl=_Cid11QosExtNotifControl_ObjectIdentity((1,3,6,1,4,1,9,10,90,1,3))
class _Cid11QosExtNotifEnabled_Type(TruthValue):defaultValue=2
_Cid11QosExtNotifEnabled_Type.__name__=_K
_Cid11QosExtNotifEnabled_Object=MibScalar
cid11QosExtNotifEnabled=_Cid11QosExtNotifEnabled_Object((1,3,6,1,4,1,9,10,90,1,3,1),_Cid11QosExtNotifEnabled_Type())
cid11QosExtNotifEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:cid11QosExtNotifEnabled.setStatus(_A)
_CiscoIetfDot11QosExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosExtMIBConform=_CiscoIetfDot11QosExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,90,2))
_CiscoIetfD11QosExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIetfD11QosExtMIBCompliances=_CiscoIetfD11QosExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,90,2,1))
_CiscoIetfD11QosExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIetfD11QosExtMIBGroups=_CiscoIetfD11QosExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,90,2,2))
cwvlWlanVlanEntry.registerAugmentions((_B,_M))
cid11QosExtVlanEntry.setIndexNames(*cwvlWlanVlanEntry.getIndexNames())
ciscoIetfD11QosExtConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,90,2,2,1))
ciscoIetfD11QosExtConfigGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoIetfD11QosExtConfigGroup.setStatus(_A)
ciscoIetfD11QosExtQueueGroup=ObjectGroup((1,3,6,1,4,1,9,10,90,2,2,2))
ciscoIetfD11QosExtQueueGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoIetfD11QosExtQueueGroup.setStatus(_A)
ciscoIetfD11QosExtNotifConGroup=ObjectGroup((1,3,6,1,4,1,9,10,90,2,2,3))
ciscoIetfD11QosExtNotifConGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoIetfD11QosExtNotifConGroup.setStatus(_A)
ciscoIetfDot11QosExtChangeNotif=NotificationType((1,3,6,1,4,1,9,10,90,0,1))
ciscoIetfDot11QosExtChangeNotif.setObjects((_C,_J))
if mibBuilder.loadTexts:ciscoIetfDot11QosExtChangeNotif.setStatus(_A)
ciscoIetfD11QosExtNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,90,2,2,4))
ciscoIetfD11QosExtNotifGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:ciscoIetfD11QosExtNotifGroup.setStatus(_A)
ciscoIetfD11QosExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,90,2,1,1))
ciscoIetfD11QosExtMIBCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoIetfD11QosExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIetfDot11QosExtMIB':ciscoIetfDot11QosExtMIB,'ciscoIetfDot11QosExtMIBNotifs':ciscoIetfDot11QosExtMIBNotifs,_T:ciscoIetfDot11QosExtChangeNotif,'ciscoIetfDot11QosExtMIBObjects':ciscoIetfDot11QosExtMIBObjects,'cid11QosExtConfig':cid11QosExtConfig,'cid11QosExtConfigTable':cid11QosExtConfigTable,'cid11QosExtConfigEntry':cid11QosExtConfigEntry,_N:cid11QosExtBackoffOffset,_O:cid11QosExtMaxRetry,'cid11QosExtIfConfigTable':cid11QosExtIfConfigTable,'cid11QosExtIfConfigEntry':cid11QosExtIfConfigEntry,_P:cid11QosExtOptionEnabled,'cid11QosExtVlanTable':cid11QosExtVlanTable,_M:cid11QosExtVlanEntry,_Q:cid11QosExtVlanClassOfService,'cid11QosExtQueue':cid11QosExtQueue,'cid11QosExtQueueTable':cid11QosExtQueueTable,'cid11QosExtQueueEntry':cid11QosExtQueueEntry,_R:cid11QosExtQueueQuota,'cid11QosExtNotifControl':cid11QosExtNotifControl,_S:cid11QosExtNotifEnabled,'ciscoIetfDot11QosExtMIBConform':ciscoIetfDot11QosExtMIBConform,'ciscoIetfD11QosExtMIBCompliances':ciscoIetfD11QosExtMIBCompliances,'ciscoIetfD11QosExtMIBCompliance':ciscoIetfD11QosExtMIBCompliance,'ciscoIetfD11QosExtMIBGroups':ciscoIetfD11QosExtMIBGroups,_U:ciscoIetfD11QosExtConfigGroup,_V:ciscoIetfD11QosExtQueueGroup,_W:ciscoIetfD11QosExtNotifConGroup,_X:ciscoIetfD11QosExtNotifGroup})