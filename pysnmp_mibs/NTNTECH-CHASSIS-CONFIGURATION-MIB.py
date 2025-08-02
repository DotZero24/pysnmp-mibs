_X='mgmtPortCfgMumIndex'
_W='advCfgMumIndex'
_V='snmpCfgNoticeIndex'
_U='uimCfgE1Index'
_T='uimCfgE1MumIndex'
_S='uimCfgT1Index'
_R='uimCfgT1MumIndex'
_Q='uimEthFull'
_P='uimEthHalf'
_O='uimEthGig'
_N='uimEth100'
_M='uimEth10'
_L='uimCfgEthIndex'
_K='uimCfgEthMumIndex'
_J='mumCfgIndex'
_I='OctetString'
_H='uimEthAutoNegotiate'
_G='enabled'
_F='disabled'
_E='read-only'
_D='NTNTECH-CHASSIS-CONFIGURATION-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtnDefaultGateway,NtnDisplayString,NtnSubnetMask,NtnTimeTicks,ntntechChassis=mibBuilder.importSymbols('NTNTECH-ROOT-MIB','NtnDefaultGateway','NtnDisplayString','NtnSubnetMask','NtnTimeTicks','ntntechChassis')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntntechChassisConfigurationMIB=ModuleIdentity((1,3,6,1,4,1,8059,1,1,1))
if mibBuilder.loadTexts:ntntechChassisConfigurationMIB.setRevisions(('1902-08-13 11:12','1902-08-28 09:12','1902-10-11 09:13','1902-10-22 02:00','1902-11-04 12:58','1904-03-15 10:15','1904-04-27 11:16','1904-10-11 09:09','1904-11-17 09:58'))
_ChsCfgMIBObjects_ObjectIdentity=ObjectIdentity
chsCfgMIBObjects=_ChsCfgMIBObjects_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1))
_ChsCfgParameterConfiguration_ObjectIdentity=ObjectIdentity
chsCfgParameterConfiguration=_ChsCfgParameterConfiguration_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1))
_PrmCfgMultiplexerUplinkModule_ObjectIdentity=ObjectIdentity
prmCfgMultiplexerUplinkModule=_PrmCfgMultiplexerUplinkModule_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1))
_MumCfgNotes_Type=NtnDisplayString
_MumCfgNotes_Object=MibScalar
mumCfgNotes=_MumCfgNotes_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,1),_MumCfgNotes_Type())
mumCfgNotes.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgNotes.setStatus(_A)
_MumCfgTable_Object=MibTable
mumCfgTable=_MumCfgTable_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2))
if mibBuilder.loadTexts:mumCfgTable.setStatus(_A)
_MumCfgEntry_Object=MibTableRow
mumCfgEntry=_MumCfgEntry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1))
mumCfgEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:mumCfgEntry.setStatus(_A)
class _MumCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MumCfgIndex_Type.__name__=_B
_MumCfgIndex_Object=MibTableColumn
mumCfgIndex=_MumCfgIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,1),_MumCfgIndex_Type())
mumCfgIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mumCfgIndex.setStatus(_A)
_MumCfgIpAddress_Type=IpAddress
_MumCfgIpAddress_Object=MibTableColumn
mumCfgIpAddress=_MumCfgIpAddress_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,2),_MumCfgIpAddress_Type())
mumCfgIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgIpAddress.setStatus(_A)
_MumCfgSubnetMask_Type=IpAddress
_MumCfgSubnetMask_Object=MibTableColumn
mumCfgSubnetMask=_MumCfgSubnetMask_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,3),_MumCfgSubnetMask_Type())
mumCfgSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgSubnetMask.setStatus(_A)
_MumCfgDefaultGateway_Type=IpAddress
_MumCfgDefaultGateway_Object=MibTableColumn
mumCfgDefaultGateway=_MumCfgDefaultGateway_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,4),_MumCfgDefaultGateway_Type())
mumCfgDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgDefaultGateway.setStatus(_A)
class _MumCfgInbandMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_MumCfgInbandMgmt_Type.__name__=_B
_MumCfgInbandMgmt_Object=MibTableColumn
mumCfgInbandMgmt=_MumCfgInbandMgmt_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,5),_MumCfgInbandMgmt_Type())
mumCfgInbandMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgInbandMgmt.setStatus(_A)
class _MumCfgInbandMGMTVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4085))
_MumCfgInbandMGMTVlanID_Type.__name__=_B
_MumCfgInbandMGMTVlanID_Object=MibTableColumn
mumCfgInbandMGMTVlanID=_MumCfgInbandMGMTVlanID_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,6),_MumCfgInbandMGMTVlanID_Type())
mumCfgInbandMGMTVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgInbandMGMTVlanID.setStatus(_A)
class _MumCfgInterConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('neither',1),('uplink1',2),('uplink2',3),('uplink3',4),('uplink4',5),('mgmt',6)))
_MumCfgInterConnection_Type.__name__=_B
_MumCfgInterConnection_Object=MibTableColumn
mumCfgInterConnection=_MumCfgInterConnection_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,7),_MumCfgInterConnection_Type())
mumCfgInterConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgInterConnection.setStatus(_A)
class _MumCfgCommitChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_MumCfgCommitChange_Type.__name__=_B
_MumCfgCommitChange_Object=MibTableColumn
mumCfgCommitChange=_MumCfgCommitChange_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,2,1,8),_MumCfgCommitChange_Type())
mumCfgCommitChange.setMaxAccess(_C)
if mibBuilder.loadTexts:mumCfgCommitChange.setStatus(_A)
_MumCfgUplinkInterfaceModule_ObjectIdentity=ObjectIdentity
mumCfgUplinkInterfaceModule=_MumCfgUplinkInterfaceModule_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,3))
_UimCfgEthTable_Object=MibTable
uimCfgEthTable=_UimCfgEthTable_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1))
if mibBuilder.loadTexts:uimCfgEthTable.setStatus(_A)
_UimCfgEthEntry_Object=MibTableRow
uimCfgEthEntry=_UimCfgEthEntry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1,1))
uimCfgEthEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:uimCfgEthEntry.setStatus(_A)
class _UimCfgEthMumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_UimCfgEthMumIndex_Type.__name__=_B
_UimCfgEthMumIndex_Object=MibTableColumn
uimCfgEthMumIndex=_UimCfgEthMumIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1,1,1),_UimCfgEthMumIndex_Type())
uimCfgEthMumIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgEthMumIndex.setStatus(_A)
class _UimCfgEthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_UimCfgEthIndex_Type.__name__=_B
_UimCfgEthIndex_Object=MibTableColumn
uimCfgEthIndex=_UimCfgEthIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1,1,2),_UimCfgEthIndex_Type())
uimCfgEthIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgEthIndex.setStatus(_A)
class _UimCfgEthRxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_M,1),(_N,2),(_O,3)))
_UimCfgEthRxTxRate_Type.__name__=_B
_UimCfgEthRxTxRate_Object=MibTableColumn
uimCfgEthRxTxRate=_UimCfgEthRxTxRate_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1,1,3),_UimCfgEthRxTxRate_Type())
uimCfgEthRxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgEthRxTxRate.setStatus(_A)
class _UimCfgEthDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_P,1),(_Q,2)))
_UimCfgEthDuplex_Type.__name__=_B
_UimCfgEthDuplex_Object=MibTableColumn
uimCfgEthDuplex=_UimCfgEthDuplex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,1,1,4),_UimCfgEthDuplex_Type())
uimCfgEthDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgEthDuplex.setStatus(_A)
_UimCfgT1Table_Object=MibTable
uimCfgT1Table=_UimCfgT1Table_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2))
if mibBuilder.loadTexts:uimCfgT1Table.setStatus(_A)
_UimCfgT1Entry_Object=MibTableRow
uimCfgT1Entry=_UimCfgT1Entry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1))
uimCfgT1Entry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:uimCfgT1Entry.setStatus(_A)
class _UimCfgT1MumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_UimCfgT1MumIndex_Type.__name__=_B
_UimCfgT1MumIndex_Object=MibTableColumn
uimCfgT1MumIndex=_UimCfgT1MumIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1,1),_UimCfgT1MumIndex_Type())
uimCfgT1MumIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgT1MumIndex.setStatus(_A)
class _UimCfgT1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_UimCfgT1Index_Type.__name__=_B
_UimCfgT1Index_Object=MibTableColumn
uimCfgT1Index=_UimCfgT1Index_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1,2),_UimCfgT1Index_Type())
uimCfgT1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgT1Index.setStatus(_A)
class _UimCfgT1Frame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uimT1ESF',1),('uimT1SFD4',2)))
_UimCfgT1Frame_Type.__name__=_B
_UimCfgT1Frame_Object=MibTableColumn
uimCfgT1Frame=_UimCfgT1Frame_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1,3),_UimCfgT1Frame_Type())
uimCfgT1Frame.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgT1Frame.setStatus(_A)
class _UimCfgT1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uimT1B8ZS',1),('uimT1AMI',2)))
_UimCfgT1LineCode_Type.__name__=_B
_UimCfgT1LineCode_Object=MibTableColumn
uimCfgT1LineCode=_UimCfgT1LineCode_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1,4),_UimCfgT1LineCode_Type())
uimCfgT1LineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgT1LineCode.setStatus(_A)
class _UimCfgT1LineBuildout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('uimT10db',1),('uimT1N7p5db',2),('uimT1N15db',3),('uimT1N22p5db',4)))
_UimCfgT1LineBuildout_Type.__name__=_B
_UimCfgT1LineBuildout_Object=MibTableColumn
uimCfgT1LineBuildout=_UimCfgT1LineBuildout_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,2,1,5),_UimCfgT1LineBuildout_Type())
uimCfgT1LineBuildout.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgT1LineBuildout.setStatus(_A)
_UimCfgE1Table_Object=MibTable
uimCfgE1Table=_UimCfgE1Table_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3))
if mibBuilder.loadTexts:uimCfgE1Table.setStatus(_A)
_UimCfgE1Entry_Object=MibTableRow
uimCfgE1Entry=_UimCfgE1Entry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3,1))
uimCfgE1Entry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:uimCfgE1Entry.setStatus(_A)
class _UimCfgE1MumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_UimCfgE1MumIndex_Type.__name__=_B
_UimCfgE1MumIndex_Object=MibTableColumn
uimCfgE1MumIndex=_UimCfgE1MumIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3,1,1),_UimCfgE1MumIndex_Type())
uimCfgE1MumIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgE1MumIndex.setStatus(_A)
class _UimCfgE1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_UimCfgE1Index_Type.__name__=_B
_UimCfgE1Index_Object=MibTableColumn
uimCfgE1Index=_UimCfgE1Index_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3,1,2),_UimCfgE1Index_Type())
uimCfgE1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:uimCfgE1Index.setStatus(_A)
class _UimCfgE1Frame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uimE1CRC',1),('uimE1NoCRC',2)))
_UimCfgE1Frame_Type.__name__=_B
_UimCfgE1Frame_Object=MibTableColumn
uimCfgE1Frame=_UimCfgE1Frame_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3,1,3),_UimCfgE1Frame_Type())
uimCfgE1Frame.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgE1Frame.setStatus(_A)
class _UimCfgE1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uimE1HDB3',1),('uimE1AMI',2)))
_UimCfgE1LineCode_Type.__name__=_B
_UimCfgE1LineCode_Object=MibTableColumn
uimCfgE1LineCode=_UimCfgE1LineCode_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,3,3,1,4),_UimCfgE1LineCode_Type())
uimCfgE1LineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:uimCfgE1LineCode.setStatus(_A)
_MumSNMPConfiguration_ObjectIdentity=ObjectIdentity
mumSNMPConfiguration=_MumSNMPConfiguration_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,4))
_SnmpCfgNoticeIpTable_Object=MibTable
snmpCfgNoticeIpTable=_SnmpCfgNoticeIpTable_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,1))
if mibBuilder.loadTexts:snmpCfgNoticeIpTable.setStatus(_A)
_SnmpCfgNoticeIpEntry_Object=MibTableRow
snmpCfgNoticeIpEntry=_SnmpCfgNoticeIpEntry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,1,1))
snmpCfgNoticeIpEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:snmpCfgNoticeIpEntry.setStatus(_A)
class _SnmpCfgNoticeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SnmpCfgNoticeIndex_Type.__name__=_B
_SnmpCfgNoticeIndex_Object=MibTableColumn
snmpCfgNoticeIndex=_SnmpCfgNoticeIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,1,1,1),_SnmpCfgNoticeIndex_Type())
snmpCfgNoticeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpCfgNoticeIndex.setStatus(_A)
_SnmpCfgNoticeIpAddress_Type=IpAddress
_SnmpCfgNoticeIpAddress_Object=MibTableColumn
snmpCfgNoticeIpAddress=_SnmpCfgNoticeIpAddress_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,1,1,2),_SnmpCfgNoticeIpAddress_Type())
snmpCfgNoticeIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCfgNoticeIpAddress.setStatus(_A)
class _SnmpCfgAuthenticationTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SnmpCfgAuthenticationTrapState_Type.__name__=_B
_SnmpCfgAuthenticationTrapState_Object=MibScalar
snmpCfgAuthenticationTrapState=_SnmpCfgAuthenticationTrapState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,2),_SnmpCfgAuthenticationTrapState_Type())
snmpCfgAuthenticationTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCfgAuthenticationTrapState.setStatus(_A)
class _SnmpCfgEnvironmentTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SnmpCfgEnvironmentTrapState_Type.__name__=_B
_SnmpCfgEnvironmentTrapState_Object=MibScalar
snmpCfgEnvironmentTrapState=_SnmpCfgEnvironmentTrapState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,3),_SnmpCfgEnvironmentTrapState_Type())
snmpCfgEnvironmentTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCfgEnvironmentTrapState.setStatus(_A)
class _SnmpCfgColdstartTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SnmpCfgColdstartTrapState_Type.__name__=_B
_SnmpCfgColdstartTrapState_Object=MibScalar
snmpCfgColdstartTrapState=_SnmpCfgColdstartTrapState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,4),_SnmpCfgColdstartTrapState_Type())
snmpCfgColdstartTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCfgColdstartTrapState.setStatus(_A)
class _SnmpCfgModulePortTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SnmpCfgModulePortTrapState_Type.__name__=_B
_SnmpCfgModulePortTrapState_Object=MibScalar
snmpCfgModulePortTrapState=_SnmpCfgModulePortTrapState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,5),_SnmpCfgModulePortTrapState_Type())
snmpCfgModulePortTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCfgModulePortTrapState.setStatus(_A)
_SnmpCfgCommunity_ObjectIdentity=ObjectIdentity
snmpCfgCommunity=_SnmpCfgCommunity_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,6))
class _ComReadWriteAccess_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ComReadWriteAccess_Type.__name__=_I
_ComReadWriteAccess_Object=MibScalar
comReadWriteAccess=_ComReadWriteAccess_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,6,1),_ComReadWriteAccess_Type())
comReadWriteAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:comReadWriteAccess.setStatus(_A)
class _ComReadOnlyAccess_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ComReadOnlyAccess_Type.__name__=_I
_ComReadOnlyAccess_Object=MibScalar
comReadOnlyAccess=_ComReadOnlyAccess_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,4,6,2),_ComReadOnlyAccess_Type())
comReadOnlyAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:comReadOnlyAccess.setStatus(_A)
_MumCfgUniques_ObjectIdentity=ObjectIdentity
mumCfgUniques=_MumCfgUniques_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,5))
class _UnqEmbHttpWebsrvrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UnqEmbHttpWebsrvrState_Type.__name__=_B
_UnqEmbHttpWebsrvrState_Object=MibScalar
unqEmbHttpWebsrvrState=_UnqEmbHttpWebsrvrState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,5,1),_UnqEmbHttpWebsrvrState_Type())
unqEmbHttpWebsrvrState.setMaxAccess(_C)
if mibBuilder.loadTexts:unqEmbHttpWebsrvrState.setStatus(_A)
_MumCfgAdvanced_ObjectIdentity=ObjectIdentity
mumCfgAdvanced=_MumCfgAdvanced_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,6))
_AdvCfgTable_Object=MibTable
advCfgTable=_AdvCfgTable_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1))
if mibBuilder.loadTexts:advCfgTable.setStatus(_A)
_AdvCfgEntry_Object=MibTableRow
advCfgEntry=_AdvCfgEntry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1))
advCfgEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:advCfgEntry.setStatus(_A)
class _AdvCfgMumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AdvCfgMumIndex_Type.__name__=_B
_AdvCfgMumIndex_Object=MibTableColumn
advCfgMumIndex=_AdvCfgMumIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,1),_AdvCfgMumIndex_Type())
advCfgMumIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:advCfgMumIndex.setStatus(_A)
class _AdvCfgTFTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_AdvCfgTFTPState_Type.__name__=_B
_AdvCfgTFTPState_Object=MibTableColumn
advCfgTFTPState=_AdvCfgTFTPState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,2),_AdvCfgTFTPState_Type())
advCfgTFTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:advCfgTFTPState.setStatus(_A)
class _AdvCfgTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_AdvCfgTelnetState_Type.__name__=_B
_AdvCfgTelnetState_Object=MibTableColumn
advCfgTelnetState=_AdvCfgTelnetState_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,3),_AdvCfgTelnetState_Type())
advCfgTelnetState.setMaxAccess(_C)
if mibBuilder.loadTexts:advCfgTelnetState.setStatus(_A)
_AdvCfgMgmtFltrIpStart_Type=IpAddress
_AdvCfgMgmtFltrIpStart_Object=MibTableColumn
advCfgMgmtFltrIpStart=_AdvCfgMgmtFltrIpStart_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,4),_AdvCfgMgmtFltrIpStart_Type())
advCfgMgmtFltrIpStart.setMaxAccess(_C)
if mibBuilder.loadTexts:advCfgMgmtFltrIpStart.setStatus(_A)
_AdvCfgMgmtFltrIpEnd_Type=IpAddress
_AdvCfgMgmtFltrIpEnd_Object=MibTableColumn
advCfgMgmtFltrIpEnd=_AdvCfgMgmtFltrIpEnd_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,5),_AdvCfgMgmtFltrIpEnd_Type())
advCfgMgmtFltrIpEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:advCfgMgmtFltrIpEnd.setStatus(_A)
_AdvCfgMgmtSessionTimeout_Type=NtnTimeTicks
_AdvCfgMgmtSessionTimeout_Object=MibTableColumn
advCfgMgmtSessionTimeout=_AdvCfgMgmtSessionTimeout_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,6,1,1,6),_AdvCfgMgmtSessionTimeout_Type())
advCfgMgmtSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:advCfgMgmtSessionTimeout.setStatus(_A)
_MumCfgManagementPort_ObjectIdentity=ObjectIdentity
mumCfgManagementPort=_MumCfgManagementPort_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1,1,1,1,7))
_MgmtPortCfgTable_Object=MibTable
mgmtPortCfgTable=_MgmtPortCfgTable_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1))
if mibBuilder.loadTexts:mgmtPortCfgTable.setStatus(_A)
_MgmtPortCfgEntry_Object=MibTableRow
mgmtPortCfgEntry=_MgmtPortCfgEntry_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1,1))
mgmtPortCfgEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:mgmtPortCfgEntry.setStatus(_A)
class _MgmtPortCfgMumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MgmtPortCfgMumIndex_Type.__name__=_B
_MgmtPortCfgMumIndex_Object=MibTableColumn
mgmtPortCfgMumIndex=_MgmtPortCfgMumIndex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1,1,1),_MgmtPortCfgMumIndex_Type())
mgmtPortCfgMumIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmtPortCfgMumIndex.setStatus(_A)
class _MgmtPortCfgRxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_M,1),(_N,2),(_O,3)))
_MgmtPortCfgRxTxRate_Type.__name__=_B
_MgmtPortCfgRxTxRate_Object=MibTableColumn
mgmtPortCfgRxTxRate=_MgmtPortCfgRxTxRate_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1,1,2),_MgmtPortCfgRxTxRate_Type())
mgmtPortCfgRxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mgmtPortCfgRxTxRate.setStatus(_A)
class _MgmtPortCfgDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_P,1),(_Q,2)))
_MgmtPortCfgDuplex_Type.__name__=_B
_MgmtPortCfgDuplex_Object=MibTableColumn
mgmtPortCfgDuplex=_MgmtPortCfgDuplex_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1,1,3),_MgmtPortCfgDuplex_Type())
mgmtPortCfgDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgmtPortCfgDuplex.setStatus(_A)
class _MgmtPortCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgmt',1),('uplink',2)))
_MgmtPortCfgType_Type.__name__=_B
_MgmtPortCfgType_Object=MibTableColumn
mgmtPortCfgType=_MgmtPortCfgType_Object((1,3,6,1,4,1,8059,1,1,1,1,1,1,7,1,1,4),_MgmtPortCfgType_Type())
mgmtPortCfgType.setMaxAccess(_C)
if mibBuilder.loadTexts:mgmtPortCfgType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ntntechChassisConfigurationMIB':ntntechChassisConfigurationMIB,'chsCfgMIBObjects':chsCfgMIBObjects,'chsCfgParameterConfiguration':chsCfgParameterConfiguration,'prmCfgMultiplexerUplinkModule':prmCfgMultiplexerUplinkModule,'mumCfgNotes':mumCfgNotes,'mumCfgTable':mumCfgTable,'mumCfgEntry':mumCfgEntry,_J:mumCfgIndex,'mumCfgIpAddress':mumCfgIpAddress,'mumCfgSubnetMask':mumCfgSubnetMask,'mumCfgDefaultGateway':mumCfgDefaultGateway,'mumCfgInbandMgmt':mumCfgInbandMgmt,'mumCfgInbandMGMTVlanID':mumCfgInbandMGMTVlanID,'mumCfgInterConnection':mumCfgInterConnection,'mumCfgCommitChange':mumCfgCommitChange,'mumCfgUplinkInterfaceModule':mumCfgUplinkInterfaceModule,'uimCfgEthTable':uimCfgEthTable,'uimCfgEthEntry':uimCfgEthEntry,_K:uimCfgEthMumIndex,_L:uimCfgEthIndex,'uimCfgEthRxTxRate':uimCfgEthRxTxRate,'uimCfgEthDuplex':uimCfgEthDuplex,'uimCfgT1Table':uimCfgT1Table,'uimCfgT1Entry':uimCfgT1Entry,_R:uimCfgT1MumIndex,_S:uimCfgT1Index,'uimCfgT1Frame':uimCfgT1Frame,'uimCfgT1LineCode':uimCfgT1LineCode,'uimCfgT1LineBuildout':uimCfgT1LineBuildout,'uimCfgE1Table':uimCfgE1Table,'uimCfgE1Entry':uimCfgE1Entry,_T:uimCfgE1MumIndex,_U:uimCfgE1Index,'uimCfgE1Frame':uimCfgE1Frame,'uimCfgE1LineCode':uimCfgE1LineCode,'mumSNMPConfiguration':mumSNMPConfiguration,'snmpCfgNoticeIpTable':snmpCfgNoticeIpTable,'snmpCfgNoticeIpEntry':snmpCfgNoticeIpEntry,_V:snmpCfgNoticeIndex,'snmpCfgNoticeIpAddress':snmpCfgNoticeIpAddress,'snmpCfgAuthenticationTrapState':snmpCfgAuthenticationTrapState,'snmpCfgEnvironmentTrapState':snmpCfgEnvironmentTrapState,'snmpCfgColdstartTrapState':snmpCfgColdstartTrapState,'snmpCfgModulePortTrapState':snmpCfgModulePortTrapState,'snmpCfgCommunity':snmpCfgCommunity,'comReadWriteAccess':comReadWriteAccess,'comReadOnlyAccess':comReadOnlyAccess,'mumCfgUniques':mumCfgUniques,'unqEmbHttpWebsrvrState':unqEmbHttpWebsrvrState,'mumCfgAdvanced':mumCfgAdvanced,'advCfgTable':advCfgTable,'advCfgEntry':advCfgEntry,_W:advCfgMumIndex,'advCfgTFTPState':advCfgTFTPState,'advCfgTelnetState':advCfgTelnetState,'advCfgMgmtFltrIpStart':advCfgMgmtFltrIpStart,'advCfgMgmtFltrIpEnd':advCfgMgmtFltrIpEnd,'advCfgMgmtSessionTimeout':advCfgMgmtSessionTimeout,'mumCfgManagementPort':mumCfgManagementPort,'mgmtPortCfgTable':mgmtPortCfgTable,'mgmtPortCfgEntry':mgmtPortCfgEntry,_X:mgmtPortCfgMumIndex,'mgmtPortCfgRxTxRate':mgmtPortCfgRxTxRate,'mgmtPortCfgDuplex':mgmtPortCfgDuplex,'mgmtPortCfgType':mgmtPortCfgType})