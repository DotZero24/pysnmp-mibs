_X='ctStatsIfIndex'
_W='ctVirtualIfPortNumber'
_V='ctVirtualIfPortIfIndex'
_U='ctVirtualIfIndex'
_T='ctSonetIfIndex'
_S='ctComPort'
_R='enabled'
_Q='disabled'
_P='ctIfPortPortNumber'
_O='ctIfPortIfNumber'
_N='standard'
_M='ctIfNumber'
_L='ifIndex'
_K='IF-MIB'
_J='OctetString'
_I='DisplayString'
_H='deprecated'
_G='enable'
_F='disable'
_E='CTIF-EXT-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctronMib2,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctronMib2')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_CommonDev_ObjectIdentity=ObjectIdentity
commonDev=_CommonDev_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,1))
class _ComDeviceTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6),ValueSizeConstraint(8,8))
_ComDeviceTime_Type.__name__=_I
_ComDeviceTime_Object=MibScalar
comDeviceTime=_ComDeviceTime_Object((1,3,6,1,4,1,52,4,3,3,1,1),_ComDeviceTime_Type())
comDeviceTime.setMaxAccess(_D)
if mibBuilder.loadTexts:comDeviceTime.setStatus(_A)
class _ComDeviceDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ComDeviceDate_Type.__name__=_I
_ComDeviceDate_Object=MibScalar
comDeviceDate=_ComDeviceDate_Object((1,3,6,1,4,1,52,4,3,3,1,2),_ComDeviceDate_Type())
comDeviceDate.setMaxAccess(_D)
if mibBuilder.loadTexts:comDeviceDate.setStatus(_A)
_ComDeviceBoardMap_Type=Integer32
_ComDeviceBoardMap_Object=MibScalar
comDeviceBoardMap=_ComDeviceBoardMap_Object((1,3,6,1,4,1,52,4,3,3,1,3),_ComDeviceBoardMap_Type())
comDeviceBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:comDeviceBoardMap.setStatus(_A)
_CtIf_ObjectIdentity=ObjectIdentity
ctIf=_CtIf_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,2))
_CtIfTable_Object=MibTable
ctIfTable=_CtIfTable_Object((1,3,6,1,4,1,52,4,3,3,2,1))
if mibBuilder.loadTexts:ctIfTable.setStatus(_A)
_CtIfEntry_Object=MibTableRow
ctIfEntry=_CtIfEntry_Object((1,3,6,1,4,1,52,4,3,3,2,1,1))
ctIfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:ctIfEntry.setStatus(_A)
_CtIfNumber_Type=Integer32
_CtIfNumber_Object=MibTableColumn
ctIfNumber=_CtIfNumber_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,1),_CtIfNumber_Type())
ctIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfNumber.setStatus(_A)
_CtIfPortCnt_Type=Integer32
_CtIfPortCnt_Object=MibTableColumn
ctIfPortCnt=_CtIfPortCnt_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,2),_CtIfPortCnt_Type())
ctIfPortCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfPortCnt.setStatus(_A)
_CtIfConnectionType_Type=ObjectIdentifier
_CtIfConnectionType_Object=MibTableColumn
ctIfConnectionType=_CtIfConnectionType_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,3),_CtIfConnectionType_Type())
ctIfConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfConnectionType.setStatus(_A)
class _CtIfLAA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CtIfLAA_Type.__name__=_J
_CtIfLAA_Object=MibTableColumn
ctIfLAA=_CtIfLAA_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,4),_CtIfLAA_Type())
ctIfLAA.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfLAA.setStatus(_A)
class _CtIfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_N,2),('full',3)))
_CtIfDuplex_Type.__name__=_C
_CtIfDuplex_Object=MibTableColumn
ctIfDuplex=_CtIfDuplex_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,5),_CtIfDuplex_Type())
ctIfDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfDuplex.setStatus(_A)
class _CtIfCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_N,2),('fullDuplex',3),('fastEthernet',4),('ethernetBased',5)))
_CtIfCapability_Type.__name__=_C
_CtIfCapability_Object=MibTableColumn
ctIfCapability=_CtIfCapability_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,6),_CtIfCapability_Type())
ctIfCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfCapability.setStatus(_A)
class _CtIfRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redundant',1),('not-redundant',2)))
_CtIfRedundancy_Type.__name__=_C
_CtIfRedundancy_Object=MibTableColumn
ctIfRedundancy=_CtIfRedundancy_Object((1,3,6,1,4,1,52,4,3,3,2,1,1,7),_CtIfRedundancy_Type())
ctIfRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfRedundancy.setStatus(_A)
_CtIfPort_ObjectIdentity=ObjectIdentity
ctIfPort=_CtIfPort_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,3))
_CtIfPortTable_Object=MibTable
ctIfPortTable=_CtIfPortTable_Object((1,3,6,1,4,1,52,4,3,3,3,1))
if mibBuilder.loadTexts:ctIfPortTable.setStatus(_A)
_CtIfPortEntry_Object=MibTableRow
ctIfPortEntry=_CtIfPortEntry_Object((1,3,6,1,4,1,52,4,3,3,3,1,1))
ctIfPortEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:ctIfPortEntry.setStatus(_A)
_CtIfPortPortNumber_Type=Integer32
_CtIfPortPortNumber_Object=MibTableColumn
ctIfPortPortNumber=_CtIfPortPortNumber_Object((1,3,6,1,4,1,52,4,3,3,3,1,1,1),_CtIfPortPortNumber_Type())
ctIfPortPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfPortPortNumber.setStatus(_A)
_CtIfPortIfNumber_Type=Integer32
_CtIfPortIfNumber_Object=MibTableColumn
ctIfPortIfNumber=_CtIfPortIfNumber_Object((1,3,6,1,4,1,52,4,3,3,3,1,1,2),_CtIfPortIfNumber_Type())
ctIfPortIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfPortIfNumber.setStatus(_A)
_CtIfPortType_Type=ObjectIdentifier
_CtIfPortType_Object=MibTableColumn
ctIfPortType=_CtIfPortType_Object((1,3,6,1,4,1,52,4,3,3,3,1,1,3),_CtIfPortType_Type())
ctIfPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfPortType.setStatus(_A)
class _CtIfPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notLinked',1),('linked',2),('notApplicable',3)))
_CtIfPortLinkStatus_Type.__name__=_C
_CtIfPortLinkStatus_Object=MibTableColumn
ctIfPortLinkStatus=_CtIfPortLinkStatus_Object((1,3,6,1,4,1,52,4,3,3,3,1,1,4),_CtIfPortLinkStatus_Type())
ctIfPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfPortLinkStatus.setStatus(_A)
class _CtIfPortTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CtIfPortTrapStatus_Type.__name__=_C
_CtIfPortTrapStatus_Object=MibTableColumn
ctIfPortTrapStatus=_CtIfPortTrapStatus_Object((1,3,6,1,4,1,52,4,3,3,3,1,1,5),_CtIfPortTrapStatus_Type())
ctIfPortTrapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfPortTrapStatus.setStatus(_A)
_CtIfCp_ObjectIdentity=ObjectIdentity
ctIfCp=_CtIfCp_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,4))
_CtCpTable_Object=MibTable
ctCpTable=_CtCpTable_Object((1,3,6,1,4,1,52,4,3,3,4,1))
if mibBuilder.loadTexts:ctCpTable.setStatus(_A)
_CtCpEntry_Object=MibTableRow
ctCpEntry=_CtCpEntry_Object((1,3,6,1,4,1,52,4,3,3,4,1,1))
ctCpEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:ctCpEntry.setStatus(_A)
_CtComPort_Type=Integer32
_CtComPort_Object=MibTableColumn
ctComPort=_CtComPort_Object((1,3,6,1,4,1,52,4,3,3,4,1,1,1),_CtComPort_Type())
ctComPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctComPort.setStatus(_A)
class _CtCpFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lm',1),('ups',2),('slip',3),('ppp',4)))
_CtCpFunction_Type.__name__=_C
_CtCpFunction_Object=MibTableColumn
ctCpFunction=_CtCpFunction_Object((1,3,6,1,4,1,52,4,3,3,4,1,1,2),_CtCpFunction_Type())
ctCpFunction.setMaxAccess(_D)
if mibBuilder.loadTexts:ctCpFunction.setStatus(_A)
_CtIfNum_Type=Integer32
_CtIfNum_Object=MibTableColumn
ctIfNum=_CtIfNum_Object((1,3,6,1,4,1,52,4,3,3,4,1,1,3),_CtIfNum_Type())
ctIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfNum.setStatus(_A)
class _CtCpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CtCpAdminStatus_Type.__name__=_C
_CtCpAdminStatus_Object=MibTableColumn
ctCpAdminStatus=_CtCpAdminStatus_Object((1,3,6,1,4,1,52,4,3,3,4,1,1,4),_CtCpAdminStatus_Type())
ctCpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctCpAdminStatus.setStatus(_A)
_CtSNMP_ObjectIdentity=ObjectIdentity
ctSNMP=_CtSNMP_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,5))
class _EnableSNMPv1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EnableSNMPv1_Type.__name__=_C
_EnableSNMPv1_Object=MibScalar
enableSNMPv1=_EnableSNMPv1_Object((1,3,6,1,4,1,52,4,3,3,5,1),_EnableSNMPv1_Type())
enableSNMPv1.setMaxAccess(_D)
if mibBuilder.loadTexts:enableSNMPv1.setStatus(_A)
class _EnableSNMPv2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EnableSNMPv2_Type.__name__=_C
_EnableSNMPv2_Object=MibScalar
enableSNMPv2=_EnableSNMPv2_Object((1,3,6,1,4,1,52,4,3,3,5,2),_EnableSNMPv2_Type())
enableSNMPv2.setMaxAccess(_D)
if mibBuilder.loadTexts:enableSNMPv2.setStatus(_A)
class _EnableSNMPv1Counter64_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EnableSNMPv1Counter64_Type.__name__=_C
_EnableSNMPv1Counter64_Object=MibScalar
enableSNMPv1Counter64=_EnableSNMPv1Counter64_Object((1,3,6,1,4,1,52,4,3,3,5,3),_EnableSNMPv1Counter64_Type())
enableSNMPv1Counter64.setMaxAccess(_D)
if mibBuilder.loadTexts:enableSNMPv1Counter64.setStatus(_A)
_CtSonet_ObjectIdentity=ObjectIdentity
ctSonet=_CtSonet_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,6))
_CtSonetTable_Object=MibTable
ctSonetTable=_CtSonetTable_Object((1,3,6,1,4,1,52,4,3,3,6,1))
if mibBuilder.loadTexts:ctSonetTable.setStatus(_H)
_CtSonetEntry_Object=MibTableRow
ctSonetEntry=_CtSonetEntry_Object((1,3,6,1,4,1,52,4,3,3,6,1,1))
ctSonetEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:ctSonetEntry.setStatus(_H)
_CtSonetIfIndex_Type=Integer32
_CtSonetIfIndex_Object=MibTableColumn
ctSonetIfIndex=_CtSonetIfIndex_Object((1,3,6,1,4,1,52,4,3,3,6,1,1,1),_CtSonetIfIndex_Type())
ctSonetIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctSonetIfIndex.setStatus(_H)
class _CtSonetMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_CtSonetMediumType_Type.__name__=_C
_CtSonetMediumType_Object=MibTableColumn
ctSonetMediumType=_CtSonetMediumType_Object((1,3,6,1,4,1,52,4,3,3,6,1,1,2),_CtSonetMediumType_Type())
ctSonetMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctSonetMediumType.setStatus(_H)
_CtVirtual_ObjectIdentity=ObjectIdentity
ctVirtual=_CtVirtual_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,7))
_CtVirtualIfTable_Object=MibTable
ctVirtualIfTable=_CtVirtualIfTable_Object((1,3,6,1,4,1,52,4,3,3,7,1))
if mibBuilder.loadTexts:ctVirtualIfTable.setStatus(_A)
_CtVirtualIfEntry_Object=MibTableRow
ctVirtualIfEntry=_CtVirtualIfEntry_Object((1,3,6,1,4,1,52,4,3,3,7,1,1))
ctVirtualIfEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:ctVirtualIfEntry.setStatus(_A)
_CtVirtualIfIndex_Type=Integer32
_CtVirtualIfIndex_Object=MibTableColumn
ctVirtualIfIndex=_CtVirtualIfIndex_Object((1,3,6,1,4,1,52,4,3,3,7,1,1,1),_CtVirtualIfIndex_Type())
ctVirtualIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfIndex.setStatus(_A)
_CtVirtualIfPhysicalInterface_Type=Integer32
_CtVirtualIfPhysicalInterface_Object=MibTableColumn
ctVirtualIfPhysicalInterface=_CtVirtualIfPhysicalInterface_Object((1,3,6,1,4,1,52,4,3,3,7,1,1,2),_CtVirtualIfPhysicalInterface_Type())
ctVirtualIfPhysicalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPhysicalInterface.setStatus(_A)
_CtVirtualIfType_Type=ObjectIdentifier
_CtVirtualIfType_Object=MibTableColumn
ctVirtualIfType=_CtVirtualIfType_Object((1,3,6,1,4,1,52,4,3,3,7,1,1,3),_CtVirtualIfType_Type())
ctVirtualIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfType.setStatus(_A)
_CtVirtualIfNumPorts_Type=Integer32
_CtVirtualIfNumPorts_Object=MibTableColumn
ctVirtualIfNumPorts=_CtVirtualIfNumPorts_Object((1,3,6,1,4,1,52,4,3,3,7,1,1,4),_CtVirtualIfNumPorts_Type())
ctVirtualIfNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfNumPorts.setStatus(_A)
_CtVirtualIfPortTable_Object=MibTable
ctVirtualIfPortTable=_CtVirtualIfPortTable_Object((1,3,6,1,4,1,52,4,3,3,7,2))
if mibBuilder.loadTexts:ctVirtualIfPortTable.setStatus(_A)
_CtVirtualIfPortEntry_Object=MibTableRow
ctVirtualIfPortEntry=_CtVirtualIfPortEntry_Object((1,3,6,1,4,1,52,4,3,3,7,2,1))
ctVirtualIfPortEntry.setIndexNames((0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:ctVirtualIfPortEntry.setStatus(_A)
_CtVirtualIfPortIfIndex_Type=Integer32
_CtVirtualIfPortIfIndex_Object=MibTableColumn
ctVirtualIfPortIfIndex=_CtVirtualIfPortIfIndex_Object((1,3,6,1,4,1,52,4,3,3,7,2,1,1),_CtVirtualIfPortIfIndex_Type())
ctVirtualIfPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPortIfIndex.setStatus(_A)
_CtVirtualIfPortNumber_Type=Integer32
_CtVirtualIfPortNumber_Object=MibTableColumn
ctVirtualIfPortNumber=_CtVirtualIfPortNumber_Object((1,3,6,1,4,1,52,4,3,3,7,2,1,2),_CtVirtualIfPortNumber_Type())
ctVirtualIfPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPortNumber.setStatus(_A)
class _CtVirtualIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('portVirtualTypeSvc',1),('portVirtualTypePvcLlc',2),('portVirtualTypePvcVcmux',3)))
_CtVirtualIfPortType_Type.__name__=_C
_CtVirtualIfPortType_Object=MibTableColumn
ctVirtualIfPortType=_CtVirtualIfPortType_Object((1,3,6,1,4,1,52,4,3,3,7,2,1,3),_CtVirtualIfPortType_Type())
ctVirtualIfPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPortType.setStatus(_A)
_CtVirtualIfPortVPI_Type=Integer32
_CtVirtualIfPortVPI_Object=MibTableColumn
ctVirtualIfPortVPI=_CtVirtualIfPortVPI_Object((1,3,6,1,4,1,52,4,3,3,7,2,1,4),_CtVirtualIfPortVPI_Type())
ctVirtualIfPortVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPortVPI.setStatus(_A)
_CtVirtualIfPortVCI_Type=Integer32
_CtVirtualIfPortVCI_Object=MibTableColumn
ctVirtualIfPortVCI=_CtVirtualIfPortVCI_Object((1,3,6,1,4,1,52,4,3,3,7,2,1,5),_CtVirtualIfPortVCI_Type())
ctVirtualIfPortVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:ctVirtualIfPortVCI.setStatus(_A)
_CtStats_ObjectIdentity=ObjectIdentity
ctStats=_CtStats_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,8))
_CtStatsTable_Object=MibTable
ctStatsTable=_CtStatsTable_Object((1,3,6,1,4,1,52,4,3,3,8,1))
if mibBuilder.loadTexts:ctStatsTable.setStatus(_A)
_CtStatsEntry_Object=MibTableRow
ctStatsEntry=_CtStatsEntry_Object((1,3,6,1,4,1,52,4,3,3,8,1,1))
ctStatsEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:ctStatsEntry.setStatus(_A)
_CtStatsIfIndex_Type=Integer32
_CtStatsIfIndex_Object=MibTableColumn
ctStatsIfIndex=_CtStatsIfIndex_Object((1,3,6,1,4,1,52,4,3,3,8,1,1,1),_CtStatsIfIndex_Type())
ctStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctStatsIfIndex.setStatus(_A)
class _CtStatsIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_CtStatsIfEnable_Type.__name__=_C
_CtStatsIfEnable_Object=MibTableColumn
ctStatsIfEnable=_CtStatsIfEnable_Object((1,3,6,1,4,1,52,4,3,3,8,1,1,2),_CtStatsIfEnable_Type())
ctStatsIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ctStatsIfEnable.setStatus(_A)
_CtFramerConfig_ObjectIdentity=ObjectIdentity
ctFramerConfig=_CtFramerConfig_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,9))
_CtIfHC_ObjectIdentity=ObjectIdentity
ctIfHC=_CtIfHC_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,10))
_CtIfHCStatsTable_Object=MibTable
ctIfHCStatsTable=_CtIfHCStatsTable_Object((1,3,6,1,4,1,52,4,3,3,10,1))
if mibBuilder.loadTexts:ctIfHCStatsTable.setStatus(_A)
_CtIfHCStatsEntry_Object=MibTableRow
ctIfHCStatsEntry=_CtIfHCStatsEntry_Object((1,3,6,1,4,1,52,4,3,3,10,1,1))
ctIfHCStatsEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:ctIfHCStatsEntry.setStatus(_A)
_CtIfInOctets_Type=Counter32
_CtIfInOctets_Object=MibTableColumn
ctIfInOctets=_CtIfInOctets_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,1),_CtIfInOctets_Type())
ctIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInOctets.setStatus(_A)
_CtIfInOctetsOverflows_Type=Counter32
_CtIfInOctetsOverflows_Object=MibTableColumn
ctIfInOctetsOverflows=_CtIfInOctetsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,2),_CtIfInOctetsOverflows_Type())
ctIfInOctetsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInOctetsOverflows.setStatus(_A)
_CtIfInUcastPkts_Type=Counter32
_CtIfInUcastPkts_Object=MibTableColumn
ctIfInUcastPkts=_CtIfInUcastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,3),_CtIfInUcastPkts_Type())
ctIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInUcastPkts.setStatus(_A)
_CtIfInUcastPktsOverflows_Type=Counter32
_CtIfInUcastPktsOverflows_Object=MibTableColumn
ctIfInUcastPktsOverflows=_CtIfInUcastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,4),_CtIfInUcastPktsOverflows_Type())
ctIfInUcastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInUcastPktsOverflows.setStatus(_A)
_CtIfInMulticastPkts_Type=Counter32
_CtIfInMulticastPkts_Object=MibTableColumn
ctIfInMulticastPkts=_CtIfInMulticastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,5),_CtIfInMulticastPkts_Type())
ctIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInMulticastPkts.setStatus(_A)
_CtIfInMulticastPktsOverflows_Type=Counter32
_CtIfInMulticastPktsOverflows_Object=MibTableColumn
ctIfInMulticastPktsOverflows=_CtIfInMulticastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,6),_CtIfInMulticastPktsOverflows_Type())
ctIfInMulticastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInMulticastPktsOverflows.setStatus(_A)
_CtIfInBroadcastPkts_Type=Counter32
_CtIfInBroadcastPkts_Object=MibTableColumn
ctIfInBroadcastPkts=_CtIfInBroadcastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,7),_CtIfInBroadcastPkts_Type())
ctIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInBroadcastPkts.setStatus(_A)
_CtIfInBroadcastPktsOverflows_Type=Counter32
_CtIfInBroadcastPktsOverflows_Object=MibTableColumn
ctIfInBroadcastPktsOverflows=_CtIfInBroadcastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,8),_CtIfInBroadcastPktsOverflows_Type())
ctIfInBroadcastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfInBroadcastPktsOverflows.setStatus(_A)
_CtIfOutOctets_Type=Counter32
_CtIfOutOctets_Object=MibTableColumn
ctIfOutOctets=_CtIfOutOctets_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,9),_CtIfOutOctets_Type())
ctIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutOctets.setStatus(_A)
_CtIfOutOctetsOverflows_Type=Counter32
_CtIfOutOctetsOverflows_Object=MibTableColumn
ctIfOutOctetsOverflows=_CtIfOutOctetsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,10),_CtIfOutOctetsOverflows_Type())
ctIfOutOctetsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutOctetsOverflows.setStatus(_A)
_CtIfOutUcastPkts_Type=Counter32
_CtIfOutUcastPkts_Object=MibTableColumn
ctIfOutUcastPkts=_CtIfOutUcastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,11),_CtIfOutUcastPkts_Type())
ctIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutUcastPkts.setStatus(_A)
_CtIfOutUcastPktsOverflows_Type=Counter32
_CtIfOutUcastPktsOverflows_Object=MibTableColumn
ctIfOutUcastPktsOverflows=_CtIfOutUcastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,12),_CtIfOutUcastPktsOverflows_Type())
ctIfOutUcastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutUcastPktsOverflows.setStatus(_A)
_CtIfOutMulticastPkts_Type=Counter32
_CtIfOutMulticastPkts_Object=MibTableColumn
ctIfOutMulticastPkts=_CtIfOutMulticastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,13),_CtIfOutMulticastPkts_Type())
ctIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutMulticastPkts.setStatus(_A)
_CtIfOutMulticastPktsOverflows_Type=Counter32
_CtIfOutMulticastPktsOverflows_Object=MibTableColumn
ctIfOutMulticastPktsOverflows=_CtIfOutMulticastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,14),_CtIfOutMulticastPktsOverflows_Type())
ctIfOutMulticastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutMulticastPktsOverflows.setStatus(_A)
_CtIfOutBroadcastPkts_Type=Counter32
_CtIfOutBroadcastPkts_Object=MibTableColumn
ctIfOutBroadcastPkts=_CtIfOutBroadcastPkts_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,15),_CtIfOutBroadcastPkts_Type())
ctIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutBroadcastPkts.setStatus(_A)
_CtIfOutBroadcastPktsOverflows_Type=Counter32
_CtIfOutBroadcastPktsOverflows_Object=MibTableColumn
ctIfOutBroadcastPktsOverflows=_CtIfOutBroadcastPktsOverflows_Object((1,3,6,1,4,1,52,4,3,3,10,1,1,16),_CtIfOutBroadcastPktsOverflows_Type())
ctIfOutBroadcastPktsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIfOutBroadcastPktsOverflows.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'commonDev':commonDev,'comDeviceTime':comDeviceTime,'comDeviceDate':comDeviceDate,'comDeviceBoardMap':comDeviceBoardMap,'ctIf':ctIf,'ctIfTable':ctIfTable,'ctIfEntry':ctIfEntry,_M:ctIfNumber,'ctIfPortCnt':ctIfPortCnt,'ctIfConnectionType':ctIfConnectionType,'ctIfLAA':ctIfLAA,'ctIfDuplex':ctIfDuplex,'ctIfCapability':ctIfCapability,'ctIfRedundancy':ctIfRedundancy,'ctIfPort':ctIfPort,'ctIfPortTable':ctIfPortTable,'ctIfPortEntry':ctIfPortEntry,_P:ctIfPortPortNumber,_O:ctIfPortIfNumber,'ctIfPortType':ctIfPortType,'ctIfPortLinkStatus':ctIfPortLinkStatus,'ctIfPortTrapStatus':ctIfPortTrapStatus,'ctIfCp':ctIfCp,'ctCpTable':ctCpTable,'ctCpEntry':ctCpEntry,_S:ctComPort,'ctCpFunction':ctCpFunction,'ctIfNum':ctIfNum,'ctCpAdminStatus':ctCpAdminStatus,'ctSNMP':ctSNMP,'enableSNMPv1':enableSNMPv1,'enableSNMPv2':enableSNMPv2,'enableSNMPv1Counter64':enableSNMPv1Counter64,'ctSonet':ctSonet,'ctSonetTable':ctSonetTable,'ctSonetEntry':ctSonetEntry,_T:ctSonetIfIndex,'ctSonetMediumType':ctSonetMediumType,'ctVirtual':ctVirtual,'ctVirtualIfTable':ctVirtualIfTable,'ctVirtualIfEntry':ctVirtualIfEntry,_U:ctVirtualIfIndex,'ctVirtualIfPhysicalInterface':ctVirtualIfPhysicalInterface,'ctVirtualIfType':ctVirtualIfType,'ctVirtualIfNumPorts':ctVirtualIfNumPorts,'ctVirtualIfPortTable':ctVirtualIfPortTable,'ctVirtualIfPortEntry':ctVirtualIfPortEntry,_V:ctVirtualIfPortIfIndex,_W:ctVirtualIfPortNumber,'ctVirtualIfPortType':ctVirtualIfPortType,'ctVirtualIfPortVPI':ctVirtualIfPortVPI,'ctVirtualIfPortVCI':ctVirtualIfPortVCI,'ctStats':ctStats,'ctStatsTable':ctStatsTable,'ctStatsEntry':ctStatsEntry,_X:ctStatsIfIndex,'ctStatsIfEnable':ctStatsIfEnable,'ctFramerConfig':ctFramerConfig,'ctIfHC':ctIfHC,'ctIfHCStatsTable':ctIfHCStatsTable,'ctIfHCStatsEntry':ctIfHCStatsEntry,'ctIfInOctets':ctIfInOctets,'ctIfInOctetsOverflows':ctIfInOctetsOverflows,'ctIfInUcastPkts':ctIfInUcastPkts,'ctIfInUcastPktsOverflows':ctIfInUcastPktsOverflows,'ctIfInMulticastPkts':ctIfInMulticastPkts,'ctIfInMulticastPktsOverflows':ctIfInMulticastPktsOverflows,'ctIfInBroadcastPkts':ctIfInBroadcastPkts,'ctIfInBroadcastPktsOverflows':ctIfInBroadcastPktsOverflows,'ctIfOutOctets':ctIfOutOctets,'ctIfOutOctetsOverflows':ctIfOutOctetsOverflows,'ctIfOutUcastPkts':ctIfOutUcastPkts,'ctIfOutUcastPktsOverflows':ctIfOutUcastPktsOverflows,'ctIfOutMulticastPkts':ctIfOutMulticastPkts,'ctIfOutMulticastPktsOverflows':ctIfOutMulticastPktsOverflows,'ctIfOutBroadcastPkts':ctIfOutBroadcastPkts,'ctIfOutBroadcastPktsOverflows':ctIfOutBroadcastPktsOverflows})