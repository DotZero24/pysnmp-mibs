_Y='cpqnBootpIfIndex'
_X='cpqnIpxIfIndex'
_W='ieee-802-2-snap'
_V='ethernet-ii'
_U='not-applicable'
_T='cpqnIpIfIndex'
_S='cpqnIPXTrapDestIndex'
_R='cpqnIPTrapDestIndex'
_Q='cpqnAclIPXIndex'
_P='no-access'
_O='cpqnAclIPIndex'
_N='cpqnVersionIndex'
_M='cpqnBaudRateIndex'
_L='cpqnBaudRatePortIndex'
_K='cpqnSPortIndex'
_J='cpqnMibModuleIndex'
_I='OctetString'
_H='disabled'
_G='enabled'
_F='DisplayString'
_E='CPQNUNIF-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class CpqnRowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('row-valid',1),('row-invalid',2)))
class IpxAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
class CpqnVersionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('hardware',2),('software',3)))
class CpqnVersionStep(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('engineering',2),('alpha',3),('beta',4),('prototype',5),('pilot',6),('pre-production',7),('production',8),('post-production',9),('simple-revision',10)))
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqnCommon_ObjectIdentity=ObjectIdentity
cpqnCommon=_CpqnCommon_ObjectIdentity((1,3,6,1,4,1,232,121))
_CpqnMibModules_ObjectIdentity=ObjectIdentity
cpqnMibModules=_CpqnMibModules_ObjectIdentity((1,3,6,1,4,1,232,121,1))
_CpqnMibModuleTable_Object=MibTable
cpqnMibModuleTable=_CpqnMibModuleTable_Object((1,3,6,1,4,1,232,121,1,1))
if mibBuilder.loadTexts:cpqnMibModuleTable.setStatus(_A)
_CpqnMibModuleEntry_Object=MibTableRow
cpqnMibModuleEntry=_CpqnMibModuleEntry_Object((1,3,6,1,4,1,232,121,1,1,1))
cpqnMibModuleEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:cpqnMibModuleEntry.setStatus(_A)
_CpqnMibModuleIndex_Type=Integer32
_CpqnMibModuleIndex_Object=MibTableColumn
cpqnMibModuleIndex=_CpqnMibModuleIndex_Object((1,3,6,1,4,1,232,121,1,1,1,1),_CpqnMibModuleIndex_Type())
cpqnMibModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnMibModuleIndex.setStatus(_A)
_CpqnMibModuleDescr_Type=DisplayString
_CpqnMibModuleDescr_Object=MibTableColumn
cpqnMibModuleDescr=_CpqnMibModuleDescr_Object((1,3,6,1,4,1,232,121,1,1,1,2),_CpqnMibModuleDescr_Type())
cpqnMibModuleDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnMibModuleDescr.setStatus(_A)
_CpqnMibModuleOid_Type=ObjectIdentifier
_CpqnMibModuleOid_Object=MibTableColumn
cpqnMibModuleOid=_CpqnMibModuleOid_Object((1,3,6,1,4,1,232,121,1,1,1,3),_CpqnMibModuleOid_Type())
cpqnMibModuleOid.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnMibModuleOid.setStatus(_A)
_CpqnUnitControl_ObjectIdentity=ObjectIdentity
cpqnUnitControl=_CpqnUnitControl_ObjectIdentity((1,3,6,1,4,1,232,121,2))
class _CpqnUnitReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('running',1),('reset',2),('warm-start',3),('reset-to-factory-values',4)))
_CpqnUnitReset_Type.__name__=_D
_CpqnUnitReset_Object=MibScalar
cpqnUnitReset=_CpqnUnitReset_Object((1,3,6,1,4,1,232,121,2,1),_CpqnUnitReset_Type())
cpqnUnitReset.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnUnitReset.setStatus(_A)
_CpqnPrimarySerialPort_Type=Integer32
_CpqnPrimarySerialPort_Object=MibScalar
cpqnPrimarySerialPort=_CpqnPrimarySerialPort_Object((1,3,6,1,4,1,232,121,2,2),_CpqnPrimarySerialPort_Type())
cpqnPrimarySerialPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnPrimarySerialPort.setStatus(_A)
_CpqnSerialPortTable_Object=MibTable
cpqnSerialPortTable=_CpqnSerialPortTable_Object((1,3,6,1,4,1,232,121,2,3))
if mibBuilder.loadTexts:cpqnSerialPortTable.setStatus(_A)
_CpqnSerialPortEntry_Object=MibTableRow
cpqnSerialPortEntry=_CpqnSerialPortEntry_Object((1,3,6,1,4,1,232,121,2,3,1))
cpqnSerialPortEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:cpqnSerialPortEntry.setStatus(_A)
_CpqnSPortIndex_Type=Integer32
_CpqnSPortIndex_Object=MibTableColumn
cpqnSPortIndex=_CpqnSPortIndex_Object((1,3,6,1,4,1,232,121,2,3,1,1),_CpqnSPortIndex_Type())
cpqnSPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnSPortIndex.setStatus(_A)
_CpqnSPortIfIndex_Type=Integer32
_CpqnSPortIfIndex_Object=MibTableColumn
cpqnSPortIfIndex=_CpqnSPortIfIndex_Object((1,3,6,1,4,1,232,121,2,3,1,2),_CpqnSPortIfIndex_Type())
cpqnSPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnSPortIfIndex.setStatus(_A)
class _CpqnSPortModemInitStringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpqnSPortModemInitStringEnable_Type.__name__=_D
_CpqnSPortModemInitStringEnable_Object=MibTableColumn
cpqnSPortModemInitStringEnable=_CpqnSPortModemInitStringEnable_Object((1,3,6,1,4,1,232,121,2,3,1,3),_CpqnSPortModemInitStringEnable_Type())
cpqnSPortModemInitStringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnSPortModemInitStringEnable.setStatus(_A)
class _CpqnSPortModemInitString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CpqnSPortModemInitString_Type.__name__=_F
_CpqnSPortModemInitString_Object=MibTableColumn
cpqnSPortModemInitString=_CpqnSPortModemInitString_Object((1,3,6,1,4,1,232,121,2,3,1,4),_CpqnSPortModemInitString_Type())
cpqnSPortModemInitString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnSPortModemInitString.setStatus(_A)
class _CpqnSPortModemAutoNegotiateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpqnSPortModemAutoNegotiateState_Type.__name__=_D
_CpqnSPortModemAutoNegotiateState_Object=MibTableColumn
cpqnSPortModemAutoNegotiateState=_CpqnSPortModemAutoNegotiateState_Object((1,3,6,1,4,1,232,121,2,3,1,5),_CpqnSPortModemAutoNegotiateState_Type())
cpqnSPortModemAutoNegotiateState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnSPortModemAutoNegotiateState.setStatus(_A)
_CpqnSPortBaudRate_Type=Integer32
_CpqnSPortBaudRate_Object=MibTableColumn
cpqnSPortBaudRate=_CpqnSPortBaudRate_Object((1,3,6,1,4,1,232,121,2,3,1,6),_CpqnSPortBaudRate_Type())
cpqnSPortBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnSPortBaudRate.setStatus(_A)
_CpqnSupportedBaudRateTable_Object=MibTable
cpqnSupportedBaudRateTable=_CpqnSupportedBaudRateTable_Object((1,3,6,1,4,1,232,121,2,4))
if mibBuilder.loadTexts:cpqnSupportedBaudRateTable.setStatus(_A)
_CpqnSupportedBaudRateEntry_Object=MibTableRow
cpqnSupportedBaudRateEntry=_CpqnSupportedBaudRateEntry_Object((1,3,6,1,4,1,232,121,2,4,1))
cpqnSupportedBaudRateEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:cpqnSupportedBaudRateEntry.setStatus(_A)
_CpqnBaudRatePortIndex_Type=Integer32
_CpqnBaudRatePortIndex_Object=MibTableColumn
cpqnBaudRatePortIndex=_CpqnBaudRatePortIndex_Object((1,3,6,1,4,1,232,121,2,4,1,1),_CpqnBaudRatePortIndex_Type())
cpqnBaudRatePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnBaudRatePortIndex.setStatus(_A)
_CpqnBaudRateIndex_Type=Integer32
_CpqnBaudRateIndex_Object=MibTableColumn
cpqnBaudRateIndex=_CpqnBaudRateIndex_Object((1,3,6,1,4,1,232,121,2,4,1,2),_CpqnBaudRateIndex_Type())
cpqnBaudRateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnBaudRateIndex.setStatus(_A)
_CpqnBaudRate_Type=Integer32
_CpqnBaudRate_Object=MibTableColumn
cpqnBaudRate=_CpqnBaudRate_Object((1,3,6,1,4,1,232,121,2,4,1,3),_CpqnBaudRate_Type())
cpqnBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnBaudRate.setStatus(_A)
_CpqnVersionInformation_ObjectIdentity=ObjectIdentity
cpqnVersionInformation=_CpqnVersionInformation_ObjectIdentity((1,3,6,1,4,1,232,121,3))
_CpqnVersionTable_Object=MibTable
cpqnVersionTable=_CpqnVersionTable_Object((1,3,6,1,4,1,232,121,3,1))
if mibBuilder.loadTexts:cpqnVersionTable.setStatus(_A)
_CpqnVersionEntry_Object=MibTableRow
cpqnVersionEntry=_CpqnVersionEntry_Object((1,3,6,1,4,1,232,121,3,1,1))
cpqnVersionEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:cpqnVersionEntry.setStatus(_A)
_CpqnVersionIndex_Type=Integer32
_CpqnVersionIndex_Object=MibTableColumn
cpqnVersionIndex=_CpqnVersionIndex_Object((1,3,6,1,4,1,232,121,3,1,1,1),_CpqnVersionIndex_Type())
cpqnVersionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionIndex.setStatus(_A)
_CpqnVersionType_Type=CpqnVersionType
_CpqnVersionType_Object=MibTableColumn
cpqnVersionType=_CpqnVersionType_Object((1,3,6,1,4,1,232,121,3,1,1,2),_CpqnVersionType_Type())
cpqnVersionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionType.setStatus(_A)
_CpqnVersionDesc_Type=DisplayString
_CpqnVersionDesc_Object=MibTableColumn
cpqnVersionDesc=_CpqnVersionDesc_Object((1,3,6,1,4,1,232,121,3,1,1,3),_CpqnVersionDesc_Type())
cpqnVersionDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionDesc.setStatus(_A)
_CpqnVersionMajor_Type=Integer32
_CpqnVersionMajor_Object=MibTableColumn
cpqnVersionMajor=_CpqnVersionMajor_Object((1,3,6,1,4,1,232,121,3,1,1,4),_CpqnVersionMajor_Type())
cpqnVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionMajor.setStatus(_A)
_CpqnVersionMinor_Type=Integer32
_CpqnVersionMinor_Object=MibTableColumn
cpqnVersionMinor=_CpqnVersionMinor_Object((1,3,6,1,4,1,232,121,3,1,1,5),_CpqnVersionMinor_Type())
cpqnVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionMinor.setStatus(_A)
_CpqnVersionStep_Type=CpqnVersionStep
_CpqnVersionStep_Object=MibTableColumn
cpqnVersionStep=_CpqnVersionStep_Object((1,3,6,1,4,1,232,121,3,1,1,6),_CpqnVersionStep_Type())
cpqnVersionStep.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionStep.setStatus(_A)
_CpqnVersionRev_Type=Integer32
_CpqnVersionRev_Object=MibTableColumn
cpqnVersionRev=_CpqnVersionRev_Object((1,3,6,1,4,1,232,121,3,1,1,7),_CpqnVersionRev_Type())
cpqnVersionRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionRev.setStatus(_A)
_CpqnVersionSerialNumber_Type=DisplayString
_CpqnVersionSerialNumber_Object=MibTableColumn
cpqnVersionSerialNumber=_CpqnVersionSerialNumber_Object((1,3,6,1,4,1,232,121,3,1,1,8),_CpqnVersionSerialNumber_Type())
cpqnVersionSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionSerialNumber.setStatus(_A)
_CpqnVersionUnitId_Type=Integer32
_CpqnVersionUnitId_Object=MibTableColumn
cpqnVersionUnitId=_CpqnVersionUnitId_Object((1,3,6,1,4,1,232,121,3,1,1,9),_CpqnVersionUnitId_Type())
cpqnVersionUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionUnitId.setStatus(_A)
_CpqnVersionParentIndex_Type=Integer32
_CpqnVersionParentIndex_Object=MibTableColumn
cpqnVersionParentIndex=_CpqnVersionParentIndex_Object((1,3,6,1,4,1,232,121,3,1,1,10),_CpqnVersionParentIndex_Type())
cpqnVersionParentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnVersionParentIndex.setStatus(_A)
_CpqnAccessControl_ObjectIdentity=ObjectIdentity
cpqnAccessControl=_CpqnAccessControl_ObjectIdentity((1,3,6,1,4,1,232,121,4))
class _CpqnAclTelnetControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpqnAclTelnetControl_Type.__name__=_D
_CpqnAclTelnetControl_Object=MibScalar
cpqnAclTelnetControl=_CpqnAclTelnetControl_Object((1,3,6,1,4,1,232,121,4,1),_CpqnAclTelnetControl_Type())
cpqnAclTelnetControl.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclTelnetControl.setStatus(_A)
_CpqnCommunityAccessIPTable_Object=MibTable
cpqnCommunityAccessIPTable=_CpqnCommunityAccessIPTable_Object((1,3,6,1,4,1,232,121,4,2))
if mibBuilder.loadTexts:cpqnCommunityAccessIPTable.setStatus(_A)
_CpqnCommAccessIPEntry_Object=MibTableRow
cpqnCommAccessIPEntry=_CpqnCommAccessIPEntry_Object((1,3,6,1,4,1,232,121,4,2,1))
cpqnCommAccessIPEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:cpqnCommAccessIPEntry.setStatus(_A)
_CpqnAclIPIndex_Type=Integer32
_CpqnAclIPIndex_Object=MibTableColumn
cpqnAclIPIndex=_CpqnAclIPIndex_Object((1,3,6,1,4,1,232,121,4,2,1,1),_CpqnAclIPIndex_Type())
cpqnAclIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnAclIPIndex.setStatus(_A)
_CpqnAclIPRowStatus_Type=CpqnRowStatus
_CpqnAclIPRowStatus_Object=MibTableColumn
cpqnAclIPRowStatus=_CpqnAclIPRowStatus_Object((1,3,6,1,4,1,232,121,4,2,1,2),_CpqnAclIPRowStatus_Type())
cpqnAclIPRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPRowStatus.setStatus(_A)
_CpqnAclIPAddrMask_Type=IpAddress
_CpqnAclIPAddrMask_Object=MibTableColumn
cpqnAclIPAddrMask=_CpqnAclIPAddrMask_Object((1,3,6,1,4,1,232,121,4,2,1,3),_CpqnAclIPAddrMask_Type())
cpqnAclIPAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPAddrMask.setStatus(_A)
_CpqnAclIPAddrMatch_Type=IpAddress
_CpqnAclIPAddrMatch_Object=MibTableColumn
cpqnAclIPAddrMatch=_CpqnAclIPAddrMatch_Object((1,3,6,1,4,1,232,121,4,2,1,4),_CpqnAclIPAddrMatch_Type())
cpqnAclIPAddrMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPAddrMatch.setStatus(_A)
class _CpqnAclIPCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CpqnAclIPCommunity_Type.__name__=_F
_CpqnAclIPCommunity_Object=MibTableColumn
cpqnAclIPCommunity=_CpqnAclIPCommunity_Object((1,3,6,1,4,1,232,121,4,2,1,5),_CpqnAclIPCommunity_Type())
cpqnAclIPCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPCommunity.setStatus(_A)
class _CpqnAclIPRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('read-only-prevent-telnet',2),('read-only-allow-telnet',3),('read-write-allow-telnet',4)))
_CpqnAclIPRights_Type.__name__=_D
_CpqnAclIPRights_Object=MibTableColumn
cpqnAclIPRights=_CpqnAclIPRights_Object((1,3,6,1,4,1,232,121,4,2,1,6),_CpqnAclIPRights_Type())
cpqnAclIPRights.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPRights.setStatus(_A)
_CpqnCommunityAccessIPXTable_Object=MibTable
cpqnCommunityAccessIPXTable=_CpqnCommunityAccessIPXTable_Object((1,3,6,1,4,1,232,121,4,3))
if mibBuilder.loadTexts:cpqnCommunityAccessIPXTable.setStatus(_A)
_CpqnCommAccessIPXEntry_Object=MibTableRow
cpqnCommAccessIPXEntry=_CpqnCommAccessIPXEntry_Object((1,3,6,1,4,1,232,121,4,3,1))
cpqnCommAccessIPXEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:cpqnCommAccessIPXEntry.setStatus(_A)
_CpqnAclIPXIndex_Type=Integer32
_CpqnAclIPXIndex_Object=MibTableColumn
cpqnAclIPXIndex=_CpqnAclIPXIndex_Object((1,3,6,1,4,1,232,121,4,3,1,1),_CpqnAclIPXIndex_Type())
cpqnAclIPXIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnAclIPXIndex.setStatus(_A)
_CpqnAclIPXRowStatus_Type=CpqnRowStatus
_CpqnAclIPXRowStatus_Object=MibTableColumn
cpqnAclIPXRowStatus=_CpqnAclIPXRowStatus_Object((1,3,6,1,4,1,232,121,4,3,1,2),_CpqnAclIPXRowStatus_Type())
cpqnAclIPXRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPXRowStatus.setStatus(_A)
_CpqnAclIPXAddrMask_Type=IpxAddress
_CpqnAclIPXAddrMask_Object=MibTableColumn
cpqnAclIPXAddrMask=_CpqnAclIPXAddrMask_Object((1,3,6,1,4,1,232,121,4,3,1,3),_CpqnAclIPXAddrMask_Type())
cpqnAclIPXAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPXAddrMask.setStatus(_A)
_CpqnAclIPXAddrMatch_Type=IpxAddress
_CpqnAclIPXAddrMatch_Object=MibTableColumn
cpqnAclIPXAddrMatch=_CpqnAclIPXAddrMatch_Object((1,3,6,1,4,1,232,121,4,3,1,4),_CpqnAclIPXAddrMatch_Type())
cpqnAclIPXAddrMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPXAddrMatch.setStatus(_A)
class _CpqnAclIPXCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CpqnAclIPXCommunity_Type.__name__=_F
_CpqnAclIPXCommunity_Object=MibTableColumn
cpqnAclIPXCommunity=_CpqnAclIPXCommunity_Object((1,3,6,1,4,1,232,121,4,3,1,5),_CpqnAclIPXCommunity_Type())
cpqnAclIPXCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPXCommunity.setStatus(_A)
class _CpqnAclIPXRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('read-only-access',2),('read-write-access',3)))
_CpqnAclIPXRights_Type.__name__=_D
_CpqnAclIPXRights_Object=MibTableColumn
cpqnAclIPXRights=_CpqnAclIPXRights_Object((1,3,6,1,4,1,232,121,4,3,1,6),_CpqnAclIPXRights_Type())
cpqnAclIPXRights.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnAclIPXRights.setStatus(_A)
_CpqnTrapDestinations_ObjectIdentity=ObjectIdentity
cpqnTrapDestinations=_CpqnTrapDestinations_ObjectIdentity((1,3,6,1,4,1,232,121,5))
_CpqnIPTrapDestTable_Object=MibTable
cpqnIPTrapDestTable=_CpqnIPTrapDestTable_Object((1,3,6,1,4,1,232,121,5,1))
if mibBuilder.loadTexts:cpqnIPTrapDestTable.setStatus(_A)
_CpqnIPTrapDestEntry_Object=MibTableRow
cpqnIPTrapDestEntry=_CpqnIPTrapDestEntry_Object((1,3,6,1,4,1,232,121,5,1,1))
cpqnIPTrapDestEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:cpqnIPTrapDestEntry.setStatus(_A)
_CpqnIPTrapDestIndex_Type=Integer32
_CpqnIPTrapDestIndex_Object=MibTableColumn
cpqnIPTrapDestIndex=_CpqnIPTrapDestIndex_Object((1,3,6,1,4,1,232,121,5,1,1,1),_CpqnIPTrapDestIndex_Type())
cpqnIPTrapDestIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIPTrapDestIndex.setStatus(_A)
_CpqnIPTrapDestRowStatus_Type=CpqnRowStatus
_CpqnIPTrapDestRowStatus_Object=MibTableColumn
cpqnIPTrapDestRowStatus=_CpqnIPTrapDestRowStatus_Object((1,3,6,1,4,1,232,121,5,1,1,2),_CpqnIPTrapDestRowStatus_Type())
cpqnIPTrapDestRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPTrapDestRowStatus.setStatus(_A)
class _CpqnIPTrapDestCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CpqnIPTrapDestCommunity_Type.__name__=_F
_CpqnIPTrapDestCommunity_Object=MibTableColumn
cpqnIPTrapDestCommunity=_CpqnIPTrapDestCommunity_Object((1,3,6,1,4,1,232,121,5,1,1,3),_CpqnIPTrapDestCommunity_Type())
cpqnIPTrapDestCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPTrapDestCommunity.setStatus(_A)
_CpqnIPTrapDestAddress_Type=IpAddress
_CpqnIPTrapDestAddress_Object=MibTableColumn
cpqnIPTrapDestAddress=_CpqnIPTrapDestAddress_Object((1,3,6,1,4,1,232,121,5,1,1,4),_CpqnIPTrapDestAddress_Type())
cpqnIPTrapDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPTrapDestAddress.setStatus(_A)
_CpqnIPXTrapDestTable_Object=MibTable
cpqnIPXTrapDestTable=_CpqnIPXTrapDestTable_Object((1,3,6,1,4,1,232,121,5,2))
if mibBuilder.loadTexts:cpqnIPXTrapDestTable.setStatus(_A)
_CpqnIPXTrapDestEntry_Object=MibTableRow
cpqnIPXTrapDestEntry=_CpqnIPXTrapDestEntry_Object((1,3,6,1,4,1,232,121,5,2,1))
cpqnIPXTrapDestEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:cpqnIPXTrapDestEntry.setStatus(_A)
_CpqnIPXTrapDestIndex_Type=Integer32
_CpqnIPXTrapDestIndex_Object=MibTableColumn
cpqnIPXTrapDestIndex=_CpqnIPXTrapDestIndex_Object((1,3,6,1,4,1,232,121,5,2,1,1),_CpqnIPXTrapDestIndex_Type())
cpqnIPXTrapDestIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIPXTrapDestIndex.setStatus(_A)
_CpqnIPXTrapDestRowStatus_Type=CpqnRowStatus
_CpqnIPXTrapDestRowStatus_Object=MibTableColumn
cpqnIPXTrapDestRowStatus=_CpqnIPXTrapDestRowStatus_Object((1,3,6,1,4,1,232,121,5,2,1,2),_CpqnIPXTrapDestRowStatus_Type())
cpqnIPXTrapDestRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPXTrapDestRowStatus.setStatus(_A)
class _CpqnIPXTrapDestCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CpqnIPXTrapDestCommunity_Type.__name__=_F
_CpqnIPXTrapDestCommunity_Object=MibTableColumn
cpqnIPXTrapDestCommunity=_CpqnIPXTrapDestCommunity_Object((1,3,6,1,4,1,232,121,5,2,1,3),_CpqnIPXTrapDestCommunity_Type())
cpqnIPXTrapDestCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPXTrapDestCommunity.setStatus(_A)
_CpqnIPXTrapDestAddress_Type=IpxAddress
_CpqnIPXTrapDestAddress_Object=MibTableColumn
cpqnIPXTrapDestAddress=_CpqnIPXTrapDestAddress_Object((1,3,6,1,4,1,232,121,5,2,1,4),_CpqnIPXTrapDestAddress_Type())
cpqnIPXTrapDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIPXTrapDestAddress.setStatus(_A)
_CpqnNetworkInfo_ObjectIdentity=ObjectIdentity
cpqnNetworkInfo=_CpqnNetworkInfo_ObjectIdentity((1,3,6,1,4,1,232,121,6))
_CpqnIpNetworkTable_Object=MibTable
cpqnIpNetworkTable=_CpqnIpNetworkTable_Object((1,3,6,1,4,1,232,121,6,1))
if mibBuilder.loadTexts:cpqnIpNetworkTable.setStatus(_A)
_CpqnIpNetworkEntry_Object=MibTableRow
cpqnIpNetworkEntry=_CpqnIpNetworkEntry_Object((1,3,6,1,4,1,232,121,6,1,1))
cpqnIpNetworkEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:cpqnIpNetworkEntry.setStatus(_A)
_CpqnIpIfIndex_Type=Integer32
_CpqnIpIfIndex_Object=MibTableColumn
cpqnIpIfIndex=_CpqnIpIfIndex_Object((1,3,6,1,4,1,232,121,6,1,1,1),_CpqnIpIfIndex_Type())
cpqnIpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIpIfIndex.setStatus(_A)
_CpqnIpPhysAddr_Type=PhysAddress
_CpqnIpPhysAddr_Object=MibTableColumn
cpqnIpPhysAddr=_CpqnIpPhysAddr_Object((1,3,6,1,4,1,232,121,6,1,1,2),_CpqnIpPhysAddr_Type())
cpqnIpPhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIpPhysAddr.setStatus(_A)
_CpqnIpAddr_Type=IpAddress
_CpqnIpAddr_Object=MibTableColumn
cpqnIpAddr=_CpqnIpAddr_Object((1,3,6,1,4,1,232,121,6,1,1,3),_CpqnIpAddr_Type())
cpqnIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpAddr.setStatus(_A)
_CpqnIpNetMask_Type=IpAddress
_CpqnIpNetMask_Object=MibTableColumn
cpqnIpNetMask=_CpqnIpNetMask_Object((1,3,6,1,4,1,232,121,6,1,1,4),_CpqnIpNetMask_Type())
cpqnIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpNetMask.setStatus(_A)
_CpqnIpRouter_Type=IpAddress
_CpqnIpRouter_Object=MibTableColumn
cpqnIpRouter=_CpqnIpRouter_Object((1,3,6,1,4,1,232,121,6,1,1,5),_CpqnIpRouter_Type())
cpqnIpRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpRouter.setStatus(_A)
class _CpqnIpFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3)))
_CpqnIpFrameType_Type.__name__=_D
_CpqnIpFrameType_Object=MibTableColumn
cpqnIpFrameType=_CpqnIpFrameType_Object((1,3,6,1,4,1,232,121,6,1,1,6),_CpqnIpFrameType_Type())
cpqnIpFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpFrameType.setStatus(_A)
class _CpqnIpAutoDiscoveryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discover',1),('do-not-discover',2)))
_CpqnIpAutoDiscoveryStatus_Type.__name__=_D
_CpqnIpAutoDiscoveryStatus_Object=MibTableColumn
cpqnIpAutoDiscoveryStatus=_CpqnIpAutoDiscoveryStatus_Object((1,3,6,1,4,1,232,121,6,1,1,7),_CpqnIpAutoDiscoveryStatus_Type())
cpqnIpAutoDiscoveryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpAutoDiscoveryStatus.setStatus(_A)
class _CpqnIpPingPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(55,65535))
_CpqnIpPingPktRate_Type.__name__=_D
_CpqnIpPingPktRate_Object=MibTableColumn
cpqnIpPingPktRate=_CpqnIpPingPktRate_Object((1,3,6,1,4,1,232,121,6,1,1,8),_CpqnIpPingPktRate_Type())
cpqnIpPingPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpPingPktRate.setStatus(_A)
class _CpqnIpInfoSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ignore-changes',1),('write-changes-to-nvram',2),('values-changed',3),('values-valid',4)))
_CpqnIpInfoSave_Type.__name__=_D
_CpqnIpInfoSave_Object=MibTableColumn
cpqnIpInfoSave=_CpqnIpInfoSave_Object((1,3,6,1,4,1,232,121,6,1,1,9),_CpqnIpInfoSave_Type())
cpqnIpInfoSave.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpInfoSave.setStatus(_A)
_CpqnIpxNetworkTable_Object=MibTable
cpqnIpxNetworkTable=_CpqnIpxNetworkTable_Object((1,3,6,1,4,1,232,121,6,2))
if mibBuilder.loadTexts:cpqnIpxNetworkTable.setStatus(_A)
_CpqnIpxNetworkEntry_Object=MibTableRow
cpqnIpxNetworkEntry=_CpqnIpxNetworkEntry_Object((1,3,6,1,4,1,232,121,6,2,1))
cpqnIpxNetworkEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:cpqnIpxNetworkEntry.setStatus(_A)
_CpqnIpxIfIndex_Type=Integer32
_CpqnIpxIfIndex_Object=MibTableColumn
cpqnIpxIfIndex=_CpqnIpxIfIndex_Object((1,3,6,1,4,1,232,121,6,2,1,1),_CpqnIpxIfIndex_Type())
cpqnIpxIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIpxIfIndex.setStatus(_A)
_CpqnIpxPhysAddr_Type=PhysAddress
_CpqnIpxPhysAddr_Object=MibTableColumn
cpqnIpxPhysAddr=_CpqnIpxPhysAddr_Object((1,3,6,1,4,1,232,121,6,2,1,2),_CpqnIpxPhysAddr_Type())
cpqnIpxPhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIpxPhysAddr.setStatus(_A)
class _CpqnIpxFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_V,2),('ethernet-802-3-raw',3),('ieee-802-2',4),(_W,5)))
_CpqnIpxFrameType_Type.__name__=_D
_CpqnIpxFrameType_Object=MibTableColumn
cpqnIpxFrameType=_CpqnIpxFrameType_Object((1,3,6,1,4,1,232,121,6,2,1,3),_CpqnIpxFrameType_Type())
cpqnIpxFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpxFrameType.setStatus(_A)
class _CpqnIpxNetworkNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CpqnIpxNetworkNumber_Type.__name__=_I
_CpqnIpxNetworkNumber_Object=MibTableColumn
cpqnIpxNetworkNumber=_CpqnIpxNetworkNumber_Object((1,3,6,1,4,1,232,121,6,2,1,4),_CpqnIpxNetworkNumber_Type())
cpqnIpxNetworkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnIpxNetworkNumber.setStatus(_A)
class _CpqnIpxSAPBcastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('do-ipx-SAPs',1),('no-ipx-SAPs',2)))
_CpqnIpxSAPBcastStatus_Type.__name__=_D
_CpqnIpxSAPBcastStatus_Object=MibTableColumn
cpqnIpxSAPBcastStatus=_CpqnIpxSAPBcastStatus_Object((1,3,6,1,4,1,232,121,6,2,1,5),_CpqnIpxSAPBcastStatus_Type())
cpqnIpxSAPBcastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnIpxSAPBcastStatus.setStatus(_A)
_CpqnBootpConfig_ObjectIdentity=ObjectIdentity
cpqnBootpConfig=_CpqnBootpConfig_ObjectIdentity((1,3,6,1,4,1,232,121,7))
_CpqnBootpTable_Object=MibTable
cpqnBootpTable=_CpqnBootpTable_Object((1,3,6,1,4,1,232,121,7,1))
if mibBuilder.loadTexts:cpqnBootpTable.setStatus(_A)
_CpqnBootpEntry_Object=MibTableRow
cpqnBootpEntry=_CpqnBootpEntry_Object((1,3,6,1,4,1,232,121,7,1,1))
cpqnBootpEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:cpqnBootpEntry.setStatus(_A)
_CpqnBootpIfIndex_Type=Integer32
_CpqnBootpIfIndex_Object=MibTableColumn
cpqnBootpIfIndex=_CpqnBootpIfIndex_Object((1,3,6,1,4,1,232,121,7,1,1,1),_CpqnBootpIfIndex_Type())
cpqnBootpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnBootpIfIndex.setStatus(_A)
class _CpqnBootpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disable-bootp',1),('enable-bootp-ethernet-ii',2),('enable-bootp-ieee-802-2-snap',3),('enable-bootp-both',4)))
_CpqnBootpEnable_Type.__name__=_D
_CpqnBootpEnable_Object=MibTableColumn
cpqnBootpEnable=_CpqnBootpEnable_Object((1,3,6,1,4,1,232,121,7,1,1,2),_CpqnBootpEnable_Type())
cpqnBootpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnBootpEnable.setStatus(_A)
class _CpqnBootpRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqnBootpRetries_Type.__name__=_D
_CpqnBootpRetries_Object=MibTableColumn
cpqnBootpRetries=_CpqnBootpRetries_Object((1,3,6,1,4,1,232,121,7,1,1,3),_CpqnBootpRetries_Type())
cpqnBootpRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnBootpRetries.setStatus(_A)
class _CpqnBootpRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_CpqnBootpRetryInterval_Type.__name__=_D
_CpqnBootpRetryInterval_Object=MibTableColumn
cpqnBootpRetryInterval=_CpqnBootpRetryInterval_Object((1,3,6,1,4,1,232,121,7,1,1,4),_CpqnBootpRetryInterval_Type())
cpqnBootpRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqnBootpRetryInterval.setStatus(_A)
_CpqnBootpServerIpAddr_Type=IpAddress
_CpqnBootpServerIpAddr_Object=MibTableColumn
cpqnBootpServerIpAddr=_CpqnBootpServerIpAddr_Object((1,3,6,1,4,1,232,121,7,1,1,5),_CpqnBootpServerIpAddr_Type())
cpqnBootpServerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqnBootpServerIpAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'CpqnRowStatus':CpqnRowStatus,'IpxAddress':IpxAddress,'CpqnVersionType':CpqnVersionType,'CpqnVersionStep':CpqnVersionStep,'compaq':compaq,'cpqnCommon':cpqnCommon,'cpqnMibModules':cpqnMibModules,'cpqnMibModuleTable':cpqnMibModuleTable,'cpqnMibModuleEntry':cpqnMibModuleEntry,_J:cpqnMibModuleIndex,'cpqnMibModuleDescr':cpqnMibModuleDescr,'cpqnMibModuleOid':cpqnMibModuleOid,'cpqnUnitControl':cpqnUnitControl,'cpqnUnitReset':cpqnUnitReset,'cpqnPrimarySerialPort':cpqnPrimarySerialPort,'cpqnSerialPortTable':cpqnSerialPortTable,'cpqnSerialPortEntry':cpqnSerialPortEntry,_K:cpqnSPortIndex,'cpqnSPortIfIndex':cpqnSPortIfIndex,'cpqnSPortModemInitStringEnable':cpqnSPortModemInitStringEnable,'cpqnSPortModemInitString':cpqnSPortModemInitString,'cpqnSPortModemAutoNegotiateState':cpqnSPortModemAutoNegotiateState,'cpqnSPortBaudRate':cpqnSPortBaudRate,'cpqnSupportedBaudRateTable':cpqnSupportedBaudRateTable,'cpqnSupportedBaudRateEntry':cpqnSupportedBaudRateEntry,_L:cpqnBaudRatePortIndex,_M:cpqnBaudRateIndex,'cpqnBaudRate':cpqnBaudRate,'cpqnVersionInformation':cpqnVersionInformation,'cpqnVersionTable':cpqnVersionTable,'cpqnVersionEntry':cpqnVersionEntry,_N:cpqnVersionIndex,'cpqnVersionType':cpqnVersionType,'cpqnVersionDesc':cpqnVersionDesc,'cpqnVersionMajor':cpqnVersionMajor,'cpqnVersionMinor':cpqnVersionMinor,'cpqnVersionStep':cpqnVersionStep,'cpqnVersionRev':cpqnVersionRev,'cpqnVersionSerialNumber':cpqnVersionSerialNumber,'cpqnVersionUnitId':cpqnVersionUnitId,'cpqnVersionParentIndex':cpqnVersionParentIndex,'cpqnAccessControl':cpqnAccessControl,'cpqnAclTelnetControl':cpqnAclTelnetControl,'cpqnCommunityAccessIPTable':cpqnCommunityAccessIPTable,'cpqnCommAccessIPEntry':cpqnCommAccessIPEntry,_O:cpqnAclIPIndex,'cpqnAclIPRowStatus':cpqnAclIPRowStatus,'cpqnAclIPAddrMask':cpqnAclIPAddrMask,'cpqnAclIPAddrMatch':cpqnAclIPAddrMatch,'cpqnAclIPCommunity':cpqnAclIPCommunity,'cpqnAclIPRights':cpqnAclIPRights,'cpqnCommunityAccessIPXTable':cpqnCommunityAccessIPXTable,'cpqnCommAccessIPXEntry':cpqnCommAccessIPXEntry,_Q:cpqnAclIPXIndex,'cpqnAclIPXRowStatus':cpqnAclIPXRowStatus,'cpqnAclIPXAddrMask':cpqnAclIPXAddrMask,'cpqnAclIPXAddrMatch':cpqnAclIPXAddrMatch,'cpqnAclIPXCommunity':cpqnAclIPXCommunity,'cpqnAclIPXRights':cpqnAclIPXRights,'cpqnTrapDestinations':cpqnTrapDestinations,'cpqnIPTrapDestTable':cpqnIPTrapDestTable,'cpqnIPTrapDestEntry':cpqnIPTrapDestEntry,_R:cpqnIPTrapDestIndex,'cpqnIPTrapDestRowStatus':cpqnIPTrapDestRowStatus,'cpqnIPTrapDestCommunity':cpqnIPTrapDestCommunity,'cpqnIPTrapDestAddress':cpqnIPTrapDestAddress,'cpqnIPXTrapDestTable':cpqnIPXTrapDestTable,'cpqnIPXTrapDestEntry':cpqnIPXTrapDestEntry,_S:cpqnIPXTrapDestIndex,'cpqnIPXTrapDestRowStatus':cpqnIPXTrapDestRowStatus,'cpqnIPXTrapDestCommunity':cpqnIPXTrapDestCommunity,'cpqnIPXTrapDestAddress':cpqnIPXTrapDestAddress,'cpqnNetworkInfo':cpqnNetworkInfo,'cpqnIpNetworkTable':cpqnIpNetworkTable,'cpqnIpNetworkEntry':cpqnIpNetworkEntry,_T:cpqnIpIfIndex,'cpqnIpPhysAddr':cpqnIpPhysAddr,'cpqnIpAddr':cpqnIpAddr,'cpqnIpNetMask':cpqnIpNetMask,'cpqnIpRouter':cpqnIpRouter,'cpqnIpFrameType':cpqnIpFrameType,'cpqnIpAutoDiscoveryStatus':cpqnIpAutoDiscoveryStatus,'cpqnIpPingPktRate':cpqnIpPingPktRate,'cpqnIpInfoSave':cpqnIpInfoSave,'cpqnIpxNetworkTable':cpqnIpxNetworkTable,'cpqnIpxNetworkEntry':cpqnIpxNetworkEntry,_X:cpqnIpxIfIndex,'cpqnIpxPhysAddr':cpqnIpxPhysAddr,'cpqnIpxFrameType':cpqnIpxFrameType,'cpqnIpxNetworkNumber':cpqnIpxNetworkNumber,'cpqnIpxSAPBcastStatus':cpqnIpxSAPBcastStatus,'cpqnBootpConfig':cpqnBootpConfig,'cpqnBootpTable':cpqnBootpTable,'cpqnBootpEntry':cpqnBootpEntry,_Y:cpqnBootpIfIndex,'cpqnBootpEnable':cpqnBootpEnable,'cpqnBootpRetries':cpqnBootpRetries,'cpqnBootpRetryInterval':cpqnBootpRetryInterval,'cpqnBootpServerIpAddr':cpqnBootpServerIpAddr})