_Z='ciscoSnmpTargetNotifSrcIntGroup'
_Y='deprecated'
_X='cExtSnmpNotifGblInformSrcIfIndex'
_W='cExtSnmpNotifGblTrapSrcIfIndex'
_V='cExtSnmpTargetVrfStatus'
_U='cExtSnmpTargetVrfStorage'
_T='cExtSnmpTargetVrfFilter'
_S='cExtSnmpTargetVrfRoute'
_R='cExtSnmpTargetAddrIntIfIndex'
_Q='cExtSnmpTargetAuthInetAddr'
_P='cExtSnmpTargetAuthInetType'
_O='cExtSnmpTargetAddrEntry'
_N='cExtSnmpTargetVrfName'
_M='read-only'
_L='StorageType'
_K='snmpTargetAddrName'
_J='SNMP-TARGET-MIB'
_I='SnmpAdminString'
_H='ciscoSnmpTargetExtVrfMIBGroup'
_G='read-write'
_F='TruthValue'
_E='ciscoSnmpTargetAuthFailureGroup'
_D='ciscoSnmpTargetExtMIBGroup'
_C='read-create'
_B='current'
_A='CISCO-SNMP-TARGET-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
snmpTargetAddrEntry,snmpTargetAddrName=mibBuilder.importSymbols(_J,'snmpTargetAddrEntry',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_L,'TextualConvention',_F)
ciscoSnmpTargetExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,412))
if mibBuilder.loadTexts:ciscoSnmpTargetExtMIB.setRevisions(('2008-11-07 00:00','2007-08-20 00:00','2004-04-01 00:00'))
_CiscoSnmpTargetExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSnmpTargetExtMIBObjects=_CiscoSnmpTargetExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,412,1))
_CExtSnmpTargetAuthAddr_ObjectIdentity=ObjectIdentity
cExtSnmpTargetAuthAddr=_CExtSnmpTargetAuthAddr_ObjectIdentity((1,3,6,1,4,1,9,9,412,1,1))
_CExtSnmpTargetAuthInetType_Type=InetAddressType
_CExtSnmpTargetAuthInetType_Object=MibScalar
cExtSnmpTargetAuthInetType=_CExtSnmpTargetAuthInetType_Object((1,3,6,1,4,1,9,9,412,1,1,1),_CExtSnmpTargetAuthInetType_Type())
cExtSnmpTargetAuthInetType.setMaxAccess(_M)
if mibBuilder.loadTexts:cExtSnmpTargetAuthInetType.setStatus(_B)
_CExtSnmpTargetAuthInetAddr_Type=InetAddress
_CExtSnmpTargetAuthInetAddr_Object=MibScalar
cExtSnmpTargetAuthInetAddr=_CExtSnmpTargetAuthInetAddr_Object((1,3,6,1,4,1,9,9,412,1,1,2),_CExtSnmpTargetAuthInetAddr_Type())
cExtSnmpTargetAuthInetAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:cExtSnmpTargetAuthInetAddr.setStatus(_B)
_CExtSnmpTargetAddrTable_Object=MibTable
cExtSnmpTargetAddrTable=_CExtSnmpTargetAddrTable_Object((1,3,6,1,4,1,9,9,412,1,2))
if mibBuilder.loadTexts:cExtSnmpTargetAddrTable.setStatus(_B)
_CExtSnmpTargetAddrEntry_Object=MibTableRow
cExtSnmpTargetAddrEntry=_CExtSnmpTargetAddrEntry_Object((1,3,6,1,4,1,9,9,412,1,2,1))
if mibBuilder.loadTexts:cExtSnmpTargetAddrEntry.setStatus(_B)
_CExtSnmpTargetAddrIntIfIndex_Type=InterfaceIndexOrZero
_CExtSnmpTargetAddrIntIfIndex_Object=MibTableColumn
cExtSnmpTargetAddrIntIfIndex=_CExtSnmpTargetAddrIntIfIndex_Object((1,3,6,1,4,1,9,9,412,1,2,1,1),_CExtSnmpTargetAddrIntIfIndex_Type())
cExtSnmpTargetAddrIntIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cExtSnmpTargetAddrIntIfIndex.setStatus(_B)
_CExtSnmpTargetVrfTable_Object=MibTable
cExtSnmpTargetVrfTable=_CExtSnmpTargetVrfTable_Object((1,3,6,1,4,1,9,9,412,1,3))
if mibBuilder.loadTexts:cExtSnmpTargetVrfTable.setStatus(_B)
_CExtSnmpTargetVrfEntry_Object=MibTableRow
cExtSnmpTargetVrfEntry=_CExtSnmpTargetVrfEntry_Object((1,3,6,1,4,1,9,9,412,1,3,1))
cExtSnmpTargetVrfEntry.setIndexNames((0,_J,_K),(0,_A,_N))
if mibBuilder.loadTexts:cExtSnmpTargetVrfEntry.setStatus(_B)
class _CExtSnmpTargetVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CExtSnmpTargetVrfName_Type.__name__=_I
_CExtSnmpTargetVrfName_Object=MibTableColumn
cExtSnmpTargetVrfName=_CExtSnmpTargetVrfName_Object((1,3,6,1,4,1,9,9,412,1,3,1,1),_CExtSnmpTargetVrfName_Type())
cExtSnmpTargetVrfName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cExtSnmpTargetVrfName.setStatus(_B)
class _CExtSnmpTargetVrfRoute_Type(TruthValue):defaultValue=2
_CExtSnmpTargetVrfRoute_Type.__name__=_F
_CExtSnmpTargetVrfRoute_Object=MibTableColumn
cExtSnmpTargetVrfRoute=_CExtSnmpTargetVrfRoute_Object((1,3,6,1,4,1,9,9,412,1,3,1,2),_CExtSnmpTargetVrfRoute_Type())
cExtSnmpTargetVrfRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:cExtSnmpTargetVrfRoute.setStatus(_B)
class _CExtSnmpTargetVrfFilter_Type(TruthValue):defaultValue=1
_CExtSnmpTargetVrfFilter_Type.__name__=_F
_CExtSnmpTargetVrfFilter_Object=MibTableColumn
cExtSnmpTargetVrfFilter=_CExtSnmpTargetVrfFilter_Object((1,3,6,1,4,1,9,9,412,1,3,1,3),_CExtSnmpTargetVrfFilter_Type())
cExtSnmpTargetVrfFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cExtSnmpTargetVrfFilter.setStatus(_B)
class _CExtSnmpTargetVrfStorage_Type(StorageType):defaultValue=3
_CExtSnmpTargetVrfStorage_Type.__name__=_L
_CExtSnmpTargetVrfStorage_Object=MibTableColumn
cExtSnmpTargetVrfStorage=_CExtSnmpTargetVrfStorage_Object((1,3,6,1,4,1,9,9,412,1,3,1,4),_CExtSnmpTargetVrfStorage_Type())
cExtSnmpTargetVrfStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:cExtSnmpTargetVrfStorage.setStatus(_B)
_CExtSnmpTargetVrfStatus_Type=RowStatus
_CExtSnmpTargetVrfStatus_Object=MibTableColumn
cExtSnmpTargetVrfStatus=_CExtSnmpTargetVrfStatus_Object((1,3,6,1,4,1,9,9,412,1,3,1,5),_CExtSnmpTargetVrfStatus_Type())
cExtSnmpTargetVrfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cExtSnmpTargetVrfStatus.setStatus(_B)
_CExtSnmpNotifGblTrapSrcIfIndex_Type=InterfaceIndexOrZero
_CExtSnmpNotifGblTrapSrcIfIndex_Object=MibScalar
cExtSnmpNotifGblTrapSrcIfIndex=_CExtSnmpNotifGblTrapSrcIfIndex_Object((1,3,6,1,4,1,9,9,412,1,4),_CExtSnmpNotifGblTrapSrcIfIndex_Type())
cExtSnmpNotifGblTrapSrcIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cExtSnmpNotifGblTrapSrcIfIndex.setStatus(_B)
_CExtSnmpNotifGblInformSrcIfIndex_Type=InterfaceIndexOrZero
_CExtSnmpNotifGblInformSrcIfIndex_Object=MibScalar
cExtSnmpNotifGblInformSrcIfIndex=_CExtSnmpNotifGblInformSrcIfIndex_Object((1,3,6,1,4,1,9,9,412,1,5),_CExtSnmpNotifGblInformSrcIfIndex_Type())
cExtSnmpNotifGblInformSrcIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cExtSnmpNotifGblInformSrcIfIndex.setStatus(_B)
_CiscoSnmpTargetExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSnmpTargetExtMIBConformance=_CiscoSnmpTargetExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,412,2))
_CiscoSnmpTargetExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSnmpTargetExtMIBCompliances=_CiscoSnmpTargetExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,412,2,1))
_CiscoSnmpTargetExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSnmpTargetExtMIBGroups=_CiscoSnmpTargetExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,412,2,2))
snmpTargetAddrEntry.registerAugmentions((_A,_O))
cExtSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
ciscoSnmpTargetAuthFailureGroup=ObjectGroup((1,3,6,1,4,1,9,9,412,2,2,1))
ciscoSnmpTargetAuthFailureGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoSnmpTargetAuthFailureGroup.setStatus(_B)
ciscoSnmpTargetExtMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,412,2,2,2))
ciscoSnmpTargetExtMIBGroup.setObjects((_A,_R))
if mibBuilder.loadTexts:ciscoSnmpTargetExtMIBGroup.setStatus(_B)
ciscoSnmpTargetExtVrfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,412,2,2,3))
ciscoSnmpTargetExtVrfMIBGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoSnmpTargetExtVrfMIBGroup.setStatus(_B)
ciscoSnmpTargetNotifSrcIntGroup=ObjectGroup((1,3,6,1,4,1,9,9,412,2,2,4))
ciscoSnmpTargetNotifSrcIntGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoSnmpTargetNotifSrcIntGroup.setStatus(_B)
ciscoSnmpTargetExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,412,2,1,1))
ciscoSnmpTargetExtMIBCompliance.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ciscoSnmpTargetExtMIBCompliance.setStatus(_Y)
ciscoSnmpTargetExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,412,2,1,2))
ciscoSnmpTargetExtMIBComplianceRev1.setObjects(*((_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:ciscoSnmpTargetExtMIBComplianceRev1.setStatus(_Y)
ciscoSnmpTargetExtMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,412,2,1,3))
ciscoSnmpTargetExtMIBComplianceRev2.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSnmpTargetExtMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoSnmpTargetExtMIB':ciscoSnmpTargetExtMIB,'ciscoSnmpTargetExtMIBObjects':ciscoSnmpTargetExtMIBObjects,'cExtSnmpTargetAuthAddr':cExtSnmpTargetAuthAddr,_P:cExtSnmpTargetAuthInetType,_Q:cExtSnmpTargetAuthInetAddr,'cExtSnmpTargetAddrTable':cExtSnmpTargetAddrTable,_O:cExtSnmpTargetAddrEntry,_R:cExtSnmpTargetAddrIntIfIndex,'cExtSnmpTargetVrfTable':cExtSnmpTargetVrfTable,'cExtSnmpTargetVrfEntry':cExtSnmpTargetVrfEntry,_N:cExtSnmpTargetVrfName,_S:cExtSnmpTargetVrfRoute,_T:cExtSnmpTargetVrfFilter,_U:cExtSnmpTargetVrfStorage,_V:cExtSnmpTargetVrfStatus,_W:cExtSnmpNotifGblTrapSrcIfIndex,_X:cExtSnmpNotifGblInformSrcIfIndex,'ciscoSnmpTargetExtMIBConformance':ciscoSnmpTargetExtMIBConformance,'ciscoSnmpTargetExtMIBCompliances':ciscoSnmpTargetExtMIBCompliances,'ciscoSnmpTargetExtMIBCompliance':ciscoSnmpTargetExtMIBCompliance,'ciscoSnmpTargetExtMIBComplianceRev1':ciscoSnmpTargetExtMIBComplianceRev1,'ciscoSnmpTargetExtMIBComplianceRev2':ciscoSnmpTargetExtMIBComplianceRev2,'ciscoSnmpTargetExtMIBGroups':ciscoSnmpTargetExtMIBGroups,_E:ciscoSnmpTargetAuthFailureGroup,_D:ciscoSnmpTargetExtMIBGroup,_H:ciscoSnmpTargetExtVrfMIBGroup,_Z:ciscoSnmpTargetNotifSrcIntGroup})