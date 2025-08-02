_R='cslbcSlbDfpCongestionGroup'
_Q='cslbcSlbDfpScalarsGroup'
_P='ciscoSlbDfpInstanceGroup'
_O='cslbcSlbDfpCongestionAbate'
_N='cslbcSlbDfpCongestionOnset'
_M='read-only'
_L='cslbcProcessorDfpValPhysicalIndex'
_K='DFP weight'
_J='read-write'
_I='Integer32'
_H='cslbcDfpCongestionAbateThreshold'
_G='cslbcDfpCongestionOnsetThreshold'
_F='CslbcDfpValue'
_E='cslbcDfpCongestionThresholdType'
_D='cslbcProcessorDfpValDfpValue'
_C='cslbcProcessorDfpValDescription'
_B='current'
_A='CISCO-SLB-DFP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSlbDfpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,689))
if mibBuilder.loadTexts:ciscoSlbDfpMIB.setRevisions(('2009-01-29 00:00',))
class CslbcDfpValue(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoSlbDfpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSlbDfpMIBNotifs=_CiscoSlbDfpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,689,0))
_CiscoSlbDfpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSlbDfpMIBObjects=_CiscoSlbDfpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,689,1))
class _CslbcDfpCongestionOnsetThreshold_Type(CslbcDfpValue):defaultValue=0
_CslbcDfpCongestionOnsetThreshold_Type.__name__=_F
_CslbcDfpCongestionOnsetThreshold_Object=MibScalar
cslbcDfpCongestionOnsetThreshold=_CslbcDfpCongestionOnsetThreshold_Object((1,3,6,1,4,1,9,9,689,1,1),_CslbcDfpCongestionOnsetThreshold_Type())
cslbcDfpCongestionOnsetThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:cslbcDfpCongestionOnsetThreshold.setStatus(_B)
if mibBuilder.loadTexts:cslbcDfpCongestionOnsetThreshold.setUnits(_K)
class _CslbcDfpCongestionAbateThreshold_Type(CslbcDfpValue):defaultValue=0
_CslbcDfpCongestionAbateThreshold_Type.__name__=_F
_CslbcDfpCongestionAbateThreshold_Object=MibScalar
cslbcDfpCongestionAbateThreshold=_CslbcDfpCongestionAbateThreshold_Object((1,3,6,1,4,1,9,9,689,1,2),_CslbcDfpCongestionAbateThreshold_Type())
cslbcDfpCongestionAbateThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:cslbcDfpCongestionAbateThreshold.setStatus(_B)
if mibBuilder.loadTexts:cslbcDfpCongestionAbateThreshold.setUnits(_K)
class _CslbcDfpCongestionThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('reject',1),('abort',2),('redirect',3),('drop',4)))
_CslbcDfpCongestionThresholdType_Type.__name__=_I
_CslbcDfpCongestionThresholdType_Object=MibScalar
cslbcDfpCongestionThresholdType=_CslbcDfpCongestionThresholdType_Object((1,3,6,1,4,1,9,9,689,1,3),_CslbcDfpCongestionThresholdType_Type())
cslbcDfpCongestionThresholdType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cslbcDfpCongestionThresholdType.setStatus(_B)
_CslbcProcessorDfpValTable_Object=MibTable
cslbcProcessorDfpValTable=_CslbcProcessorDfpValTable_Object((1,3,6,1,4,1,9,9,689,1,4))
if mibBuilder.loadTexts:cslbcProcessorDfpValTable.setStatus(_B)
_CslbcProcessorDfpValEntry_Object=MibTableRow
cslbcProcessorDfpValEntry=_CslbcProcessorDfpValEntry_Object((1,3,6,1,4,1,9,9,689,1,4,1))
cslbcProcessorDfpValEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:cslbcProcessorDfpValEntry.setStatus(_B)
_CslbcProcessorDfpValPhysicalIndex_Type=EntPhysicalIndexOrZero
_CslbcProcessorDfpValPhysicalIndex_Object=MibTableColumn
cslbcProcessorDfpValPhysicalIndex=_CslbcProcessorDfpValPhysicalIndex_Object((1,3,6,1,4,1,9,9,689,1,4,1,1),_CslbcProcessorDfpValPhysicalIndex_Type())
cslbcProcessorDfpValPhysicalIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cslbcProcessorDfpValPhysicalIndex.setStatus(_B)
_CslbcProcessorDfpValDescription_Type=SnmpAdminString
_CslbcProcessorDfpValDescription_Object=MibTableColumn
cslbcProcessorDfpValDescription=_CslbcProcessorDfpValDescription_Object((1,3,6,1,4,1,9,9,689,1,4,1,2),_CslbcProcessorDfpValDescription_Type())
cslbcProcessorDfpValDescription.setMaxAccess(_M)
if mibBuilder.loadTexts:cslbcProcessorDfpValDescription.setStatus(_B)
_CslbcProcessorDfpValDfpValue_Type=CslbcDfpValue
_CslbcProcessorDfpValDfpValue_Object=MibTableColumn
cslbcProcessorDfpValDfpValue=_CslbcProcessorDfpValDfpValue_Object((1,3,6,1,4,1,9,9,689,1,4,1,3),_CslbcProcessorDfpValDfpValue_Type())
cslbcProcessorDfpValDfpValue.setMaxAccess(_M)
if mibBuilder.loadTexts:cslbcProcessorDfpValDfpValue.setStatus(_B)
_CiscoSlbDfpMIBConform_ObjectIdentity=ObjectIdentity
ciscoSlbDfpMIBConform=_CiscoSlbDfpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,689,2))
_CiscoSlbDfpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSlbDfpMIBCompliances=_CiscoSlbDfpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,689,2,1))
_CiscoSlbDfpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSlbDfpMIBGroups=_CiscoSlbDfpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,689,2,2))
ciscoSlbDfpInstanceGroup=ObjectGroup((1,3,6,1,4,1,9,9,689,2,2,1))
ciscoSlbDfpInstanceGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoSlbDfpInstanceGroup.setStatus(_B)
cslbcSlbDfpScalarsGroup=ObjectGroup((1,3,6,1,4,1,9,9,689,2,2,2))
cslbcSlbDfpScalarsGroup.setObjects(*((_A,_G),(_A,_H),(_A,_E)))
if mibBuilder.loadTexts:cslbcSlbDfpScalarsGroup.setStatus(_B)
cslbcSlbDfpCongestionOnset=NotificationType((1,3,6,1,4,1,9,9,689,0,1))
cslbcSlbDfpCongestionOnset.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:cslbcSlbDfpCongestionOnset.setStatus(_B)
cslbcSlbDfpCongestionAbate=NotificationType((1,3,6,1,4,1,9,9,689,0,2))
cslbcSlbDfpCongestionAbate.setObjects(*((_A,_C),(_A,_D),(_A,_H),(_A,_E)))
if mibBuilder.loadTexts:cslbcSlbDfpCongestionAbate.setStatus(_B)
cslbcSlbDfpCongestionGroup=NotificationGroup((1,3,6,1,4,1,9,9,689,2,2,3))
cslbcSlbDfpCongestionGroup.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:cslbcSlbDfpCongestionGroup.setStatus(_B)
ciscoSlbDfpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,689,2,1,1))
ciscoSlbDfpMIBCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoSlbDfpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_F:CslbcDfpValue,'ciscoSlbDfpMIB':ciscoSlbDfpMIB,'ciscoSlbDfpMIBNotifs':ciscoSlbDfpMIBNotifs,_N:cslbcSlbDfpCongestionOnset,_O:cslbcSlbDfpCongestionAbate,'ciscoSlbDfpMIBObjects':ciscoSlbDfpMIBObjects,_G:cslbcDfpCongestionOnsetThreshold,_H:cslbcDfpCongestionAbateThreshold,_E:cslbcDfpCongestionThresholdType,'cslbcProcessorDfpValTable':cslbcProcessorDfpValTable,'cslbcProcessorDfpValEntry':cslbcProcessorDfpValEntry,_L:cslbcProcessorDfpValPhysicalIndex,_C:cslbcProcessorDfpValDescription,_D:cslbcProcessorDfpValDfpValue,'ciscoSlbDfpMIBConform':ciscoSlbDfpMIBConform,'ciscoSlbDfpMIBCompliances':ciscoSlbDfpMIBCompliances,'ciscoSlbDfpMIBCompliance':ciscoSlbDfpMIBCompliance,'ciscoSlbDfpMIBGroups':ciscoSlbDfpMIBGroups,_P:ciscoSlbDfpInstanceGroup,_Q:cslbcSlbDfpScalarsGroup,_R:cslbcSlbDfpCongestionGroup})