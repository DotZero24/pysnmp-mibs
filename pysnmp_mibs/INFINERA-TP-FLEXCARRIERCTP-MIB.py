_H='flexCarrierCtpGroup'
_G='flexCarrierCtpFreqSlotList'
_F='flexCarrierCtpPmHistStatsEnable'
_E='read-write'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-FLEXCARRIERCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnModulation,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnModulation','InfnPmHistStatsControl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
flexCarrierCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,59))
_FlexCarrierCtpTable_Object=MibTable
flexCarrierCtpTable=_FlexCarrierCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,59,1))
if mibBuilder.loadTexts:flexCarrierCtpTable.setStatus(_A)
_FlexCarrierCtpEntry_Object=MibTableRow
flexCarrierCtpEntry=_FlexCarrierCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,59,1,1))
flexCarrierCtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:flexCarrierCtpEntry.setStatus(_A)
_FlexCarrierCtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FlexCarrierCtpPmHistStatsEnable_Object=MibTableColumn
flexCarrierCtpPmHistStatsEnable=_FlexCarrierCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,59,1,1,1),_FlexCarrierCtpPmHistStatsEnable_Type())
flexCarrierCtpPmHistStatsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:flexCarrierCtpPmHistStatsEnable.setStatus(_A)
_FlexCarrierCtpFreqSlotList_Type=DisplayString
_FlexCarrierCtpFreqSlotList_Object=MibTableColumn
flexCarrierCtpFreqSlotList=_FlexCarrierCtpFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,59,1,1,2),_FlexCarrierCtpFreqSlotList_Type())
flexCarrierCtpFreqSlotList.setMaxAccess(_E)
if mibBuilder.loadTexts:flexCarrierCtpFreqSlotList.setStatus(_A)
_FlexCarrierCtpConformance_ObjectIdentity=ObjectIdentity
flexCarrierCtpConformance=_FlexCarrierCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,59,59))
_FlexCarrierCtpCompliances_ObjectIdentity=ObjectIdentity
flexCarrierCtpCompliances=_FlexCarrierCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,59,59,1))
_FlexCarrierCtpGroups_ObjectIdentity=ObjectIdentity
flexCarrierCtpGroups=_FlexCarrierCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,59,59,2))
flexCarrierCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,59,59,2,1))
flexCarrierCtpGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:flexCarrierCtpGroup.setStatus(_A)
flexCarrierCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,59,59,1,1))
flexCarrierCtpCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:flexCarrierCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'flexCarrierCtpMIB':flexCarrierCtpMIB,'flexCarrierCtpTable':flexCarrierCtpTable,'flexCarrierCtpEntry':flexCarrierCtpEntry,_F:flexCarrierCtpPmHistStatsEnable,_G:flexCarrierCtpFreqSlotList,'flexCarrierCtpConformance':flexCarrierCtpConformance,'flexCarrierCtpCompliances':flexCarrierCtpCompliances,'flexCarrierCtpCompliance':flexCarrierCtpCompliance,'flexCarrierCtpGroups':flexCarrierCtpGroups,_H:flexCarrierCtpGroup})