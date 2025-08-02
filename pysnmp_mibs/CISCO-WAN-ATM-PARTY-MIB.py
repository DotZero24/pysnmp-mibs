_Y='ciscoWanAtmPartyGroup'
_X='cwapRowStatus'
_W='cwapRootPhysicalId'
_V='cwapUploadCounter'
_U='cwapIdentifier'
_T='cwapReroute'
_S='cwapOperStatus'
_R='cwapAdminStatus'
_Q='cwapVci'
_P='cwapVpi'
_O='cwapNSAPAddress'
_N='WanPartyAdminStatus'
_M='cwapReference'
_L='cwapRootVci'
_K='cwapRootVpi'
_J='TruthValue'
_I='ifIndex'
_H='IF-MIB'
_G='not-accessible'
_F='Unsigned32'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='CISCO-WAN-ATM-PARTY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
ciscoWanAtmPartyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99998))
if mibBuilder.loadTexts:ciscoWanAtmPartyMIB.setRevisions(('2002-06-17 00:00',))
class WanPartyAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class WanPartyOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('fail',2)))
class WanNsapAtmAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_CiscoWanAtmPartyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWanAtmPartyMIBNotifs=_CiscoWanAtmPartyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,99998,0))
_CiscoWanAtmPartyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanAtmPartyMIBObjects=_CiscoWanAtmPartyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99998,1))
_CwapConfig_ObjectIdentity=ObjectIdentity
cwapConfig=_CwapConfig_ObjectIdentity((1,3,6,1,4,1,9,9,99998,1,1))
_CwapConfigTable_Object=MibTable
cwapConfigTable=_CwapConfigTable_Object((1,3,6,1,4,1,9,9,99998,1,1,1))
if mibBuilder.loadTexts:cwapConfigTable.setStatus(_A)
_CwapConfigEntry_Object=MibTableRow
cwapConfigEntry=_CwapConfigEntry_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1))
cwapConfigEntry.setIndexNames((0,_H,_I),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cwapConfigEntry.setStatus(_A)
class _CwapRootVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwapRootVpi_Type.__name__=_C
_CwapRootVpi_Object=MibTableColumn
cwapRootVpi=_CwapRootVpi_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,1),_CwapRootVpi_Type())
cwapRootVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwapRootVpi.setStatus(_A)
class _CwapRootVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwapRootVci_Type.__name__=_C
_CwapRootVci_Object=MibTableColumn
cwapRootVci=_CwapRootVci_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,2),_CwapRootVci_Type())
cwapRootVci.setMaxAccess(_G)
if mibBuilder.loadTexts:cwapRootVci.setStatus(_A)
class _CwapReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwapReference_Type.__name__=_C
_CwapReference_Object=MibTableColumn
cwapReference=_CwapReference_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,3),_CwapReference_Type())
cwapReference.setMaxAccess(_G)
if mibBuilder.loadTexts:cwapReference.setStatus(_A)
_CwapNSAPAddress_Type=WanNsapAtmAddress
_CwapNSAPAddress_Object=MibTableColumn
cwapNSAPAddress=_CwapNSAPAddress_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,4),_CwapNSAPAddress_Type())
cwapNSAPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapNSAPAddress.setStatus(_A)
class _CwapVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwapVpi_Type.__name__=_C
_CwapVpi_Object=MibTableColumn
cwapVpi=_CwapVpi_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,5),_CwapVpi_Type())
cwapVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapVpi.setStatus(_A)
class _CwapVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwapVci_Type.__name__=_C
_CwapVci_Object=MibTableColumn
cwapVci=_CwapVci_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,6),_CwapVci_Type())
cwapVci.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapVci.setStatus(_A)
class _CwapReroute_Type(TruthValue):defaultValue=2
_CwapReroute_Type.__name__=_J
_CwapReroute_Object=MibTableColumn
cwapReroute=_CwapReroute_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,7),_CwapReroute_Type())
cwapReroute.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapReroute.setStatus(_A)
class _CwapAdminStatus_Type(WanPartyAdminStatus):defaultValue=1
_CwapAdminStatus_Type.__name__=_N
_CwapAdminStatus_Object=MibTableColumn
cwapAdminStatus=_CwapAdminStatus_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,8),_CwapAdminStatus_Type())
cwapAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapAdminStatus.setStatus(_A)
_CwapOperStatus_Type=WanPartyOperStatus
_CwapOperStatus_Object=MibTableColumn
cwapOperStatus=_CwapOperStatus_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,9),_CwapOperStatus_Type())
cwapOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cwapOperStatus.setStatus(_A)
class _CwapIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwapIdentifier_Type.__name__=_F
_CwapIdentifier_Object=MibTableColumn
cwapIdentifier=_CwapIdentifier_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,10),_CwapIdentifier_Type())
cwapIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:cwapIdentifier.setStatus(_A)
class _CwapUploadCounter_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwapUploadCounter_Type.__name__=_F
_CwapUploadCounter_Object=MibTableColumn
cwapUploadCounter=_CwapUploadCounter_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,11),_CwapUploadCounter_Type())
cwapUploadCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:cwapUploadCounter.setStatus(_A)
_CwapRootPhysicalId_Type=DisplayString
_CwapRootPhysicalId_Object=MibTableColumn
cwapRootPhysicalId=_CwapRootPhysicalId_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,12),_CwapRootPhysicalId_Type())
cwapRootPhysicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwapRootPhysicalId.setStatus(_A)
_CwapRowStatus_Type=RowStatus
_CwapRowStatus_Object=MibTableColumn
cwapRowStatus=_CwapRowStatus_Object((1,3,6,1,4,1,9,9,99998,1,1,1,1,13),_CwapRowStatus_Type())
cwapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwapRowStatus.setStatus(_A)
_CiscoWanAtmPartyMIBConform_ObjectIdentity=ObjectIdentity
ciscoWanAtmPartyMIBConform=_CiscoWanAtmPartyMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,99998,2))
_CiscoWanAtmPartyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanAtmPartyMIBCompliances=_CiscoWanAtmPartyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99998,2,1))
_CiscoWanAtmPartyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanAtmPartyMIBGroups=_CiscoWanAtmPartyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99998,2,2))
ciscoWanAtmPartyGroup=ObjectGroup((1,3,6,1,4,1,9,9,99998,2,2,2))
ciscoWanAtmPartyGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoWanAtmPartyGroup.setStatus(_A)
ciscoWanAtmPartyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99998,2,1,1))
ciscoWanAtmPartyMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:ciscoWanAtmPartyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:WanPartyAdminStatus,'WanPartyOperStatus':WanPartyOperStatus,'WanNsapAtmAddress':WanNsapAtmAddress,'ciscoWanAtmPartyMIB':ciscoWanAtmPartyMIB,'ciscoWanAtmPartyMIBNotifs':ciscoWanAtmPartyMIBNotifs,'ciscoWanAtmPartyMIBObjects':ciscoWanAtmPartyMIBObjects,'cwapConfig':cwapConfig,'cwapConfigTable':cwapConfigTable,'cwapConfigEntry':cwapConfigEntry,_K:cwapRootVpi,_L:cwapRootVci,_M:cwapReference,_O:cwapNSAPAddress,_P:cwapVpi,_Q:cwapVci,_T:cwapReroute,_R:cwapAdminStatus,_S:cwapOperStatus,_U:cwapIdentifier,_V:cwapUploadCounter,_W:cwapRootPhysicalId,_X:cwapRowStatus,'ciscoWanAtmPartyMIBConform':ciscoWanAtmPartyMIBConform,'ciscoWanAtmPartyMIBCompliances':ciscoWanAtmPartyMIBCompliances,'ciscoWanAtmPartyMIBCompliance':ciscoWanAtmPartyMIBCompliance,'ciscoWanAtmPartyMIBGroups':ciscoWanAtmPartyMIBGroups,_Y:ciscoWanAtmPartyGroup})