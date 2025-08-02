_L='ciscoCat6kNatStatGroup'
_K='ciscoCat6kNatResourceUtilization'
_J='ciscoCat6kNatTotalEntryCount'
_I='ciscoCat6kNatOtherEntryUtilization'
_H='ciscoCat6kNatStaticEntryUtilization'
_G='ciscoCat6kNatDynamicEntryUtilization'
_F='ciscoCat6kNatFlowRecord'
_E='ciscoCat6kNatNetFlowType'
_D='ciscoCat6kNatType'
_C='read-only'
_B='CISCO-CAT6k-NAT-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCat6kNatStatMIB=ModuleIdentity((1,3,6,1,4,1,9,9,861))
if mibBuilder.loadTexts:ciscoCat6kNatStatMIB.setRevisions(('2019-06-11 00:00',))
class NatType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('static',1),('dynamic',2),('mixed',3),('other',4)))
class NetFlowType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer3',1),('mixed',2)))
class NatBool(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_CiscoCat6kNatStatMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCat6kNatStatMIBObjects=_CiscoCat6kNatStatMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,861,1))
_CiscoCat6kNatStatus_ObjectIdentity=ObjectIdentity
ciscoCat6kNatStatus=_CiscoCat6kNatStatus_ObjectIdentity((1,3,6,1,4,1,9,9,861,1,2))
_CiscoCat6kNatType_Type=NatType
_CiscoCat6kNatType_Object=MibScalar
ciscoCat6kNatType=_CiscoCat6kNatType_Object((1,3,6,1,4,1,9,9,861,1,2,1),_CiscoCat6kNatType_Type())
ciscoCat6kNatType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatType.setStatus(_A)
_CiscoCat6kNatNetFlowType_Type=NetFlowType
_CiscoCat6kNatNetFlowType_Object=MibScalar
ciscoCat6kNatNetFlowType=_CiscoCat6kNatNetFlowType_Object((1,3,6,1,4,1,9,9,861,1,2,2),_CiscoCat6kNatNetFlowType_Type())
ciscoCat6kNatNetFlowType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatNetFlowType.setStatus(_A)
_CiscoCat6kNatFlowRecord_Type=NatBool
_CiscoCat6kNatFlowRecord_Object=MibScalar
ciscoCat6kNatFlowRecord=_CiscoCat6kNatFlowRecord_Object((1,3,6,1,4,1,9,9,861,1,2,3),_CiscoCat6kNatFlowRecord_Type())
ciscoCat6kNatFlowRecord.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatFlowRecord.setStatus(_A)
_CiscoCat6kNatDynamicEntryUtilization_Type=OctetString
_CiscoCat6kNatDynamicEntryUtilization_Object=MibScalar
ciscoCat6kNatDynamicEntryUtilization=_CiscoCat6kNatDynamicEntryUtilization_Object((1,3,6,1,4,1,9,9,861,1,2,4),_CiscoCat6kNatDynamicEntryUtilization_Type())
ciscoCat6kNatDynamicEntryUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatDynamicEntryUtilization.setStatus(_A)
_CiscoCat6kNatStaticEntryUtilization_Type=OctetString
_CiscoCat6kNatStaticEntryUtilization_Object=MibScalar
ciscoCat6kNatStaticEntryUtilization=_CiscoCat6kNatStaticEntryUtilization_Object((1,3,6,1,4,1,9,9,861,1,2,5),_CiscoCat6kNatStaticEntryUtilization_Type())
ciscoCat6kNatStaticEntryUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatStaticEntryUtilization.setStatus(_A)
_CiscoCat6kNatOtherEntryUtilization_Type=OctetString
_CiscoCat6kNatOtherEntryUtilization_Object=MibScalar
ciscoCat6kNatOtherEntryUtilization=_CiscoCat6kNatOtherEntryUtilization_Object((1,3,6,1,4,1,9,9,861,1,2,6),_CiscoCat6kNatOtherEntryUtilization_Type())
ciscoCat6kNatOtherEntryUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatOtherEntryUtilization.setStatus(_A)
_CiscoCat6kNatTotalEntryCount_Type=Counter32
_CiscoCat6kNatTotalEntryCount_Object=MibScalar
ciscoCat6kNatTotalEntryCount=_CiscoCat6kNatTotalEntryCount_Object((1,3,6,1,4,1,9,9,861,1,2,7),_CiscoCat6kNatTotalEntryCount_Type())
ciscoCat6kNatTotalEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatTotalEntryCount.setStatus(_A)
_CiscoCat6kNatResourceUtilization_Type=OctetString
_CiscoCat6kNatResourceUtilization_Object=MibScalar
ciscoCat6kNatResourceUtilization=_CiscoCat6kNatResourceUtilization_Object((1,3,6,1,4,1,9,9,861,1,2,8),_CiscoCat6kNatResourceUtilization_Type())
ciscoCat6kNatResourceUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCat6kNatResourceUtilization.setStatus(_A)
_CiscoCat6kNatStatMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCat6kNatStatMIBConformance=_CiscoCat6kNatStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,861,2))
_CiscoCat6kNatStatMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCat6kNatStatMIBCompliances=_CiscoCat6kNatStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,861,2,1))
_CiscoCat6kNatStatMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCat6kNatStatMIBGroups=_CiscoCat6kNatStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,861,2,2))
ciscoCat6kNatStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,861,2,2,1))
ciscoCat6kNatStatGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoCat6kNatStatGroup.setStatus(_A)
ciscoCat6kNatStatMIBComplianceVer1=ModuleCompliance((1,3,6,1,4,1,9,9,861,2,1,1))
ciscoCat6kNatStatMIBComplianceVer1.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoCat6kNatStatMIBComplianceVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NatType':NatType,'NetFlowType':NetFlowType,'NatBool':NatBool,'ciscoCat6kNatStatMIB':ciscoCat6kNatStatMIB,'ciscoCat6kNatStatMIBObjects':ciscoCat6kNatStatMIBObjects,'ciscoCat6kNatStatus':ciscoCat6kNatStatus,_D:ciscoCat6kNatType,_E:ciscoCat6kNatNetFlowType,_F:ciscoCat6kNatFlowRecord,_G:ciscoCat6kNatDynamicEntryUtilization,_H:ciscoCat6kNatStaticEntryUtilization,_I:ciscoCat6kNatOtherEntryUtilization,_J:ciscoCat6kNatTotalEntryCount,_K:ciscoCat6kNatResourceUtilization,'ciscoCat6kNatStatMIBConformance':ciscoCat6kNatStatMIBConformance,'ciscoCat6kNatStatMIBCompliances':ciscoCat6kNatStatMIBCompliances,'ciscoCat6kNatStatMIBComplianceVer1':ciscoCat6kNatStatMIBComplianceVer1,'ciscoCat6kNatStatMIBGroups':ciscoCat6kNatStatMIBGroups,_L:ciscoCat6kNatStatGroup})