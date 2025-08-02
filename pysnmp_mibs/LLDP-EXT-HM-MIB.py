_p='lldpXHmConfigPTPEntry'
_o='lldpXHmConfigPortSecEntry'
_n='lldpXHmConfigIGMPEntry'
_m='lldpXHmConfigGMRPEntry'
_l='simplemode'
_k='multidomain'
_j='grandmaster'
_i='boundary'
_h='transparent'
_g='master'
_f='disabled'
_e='ptp2UdpIpv6'
_d='ptp2UdpIpv4'
_c='ptp2Ieee8023'
_b='ptpv2enabled'
_a='ptpv1enabled'
_Z='ptptccapable'
_Y='ptpv2capable'
_X='ptpv1capable'
_W='swsupport'
_V='automatic'
_U='forceUnauthorized'
_T='forceAuthorized'
_S='iGMPv3'
_R='iGMPv2'
_Q='iGMPv1'
_P='forwardUnregistered'
_O='forwardAll'
_N='Bits'
_M='OctetString'
_L='read-write'
_K='LLDP-EXT-HM-MIB'
_J='TruthValue'
_I='lldpRemTimeMark'
_H='lldpRemLocalPortNum'
_G='lldpRemIndex'
_F='lldpLocPortNum'
_E='Integer32'
_D='notApplicable'
_C='LLDP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpExtensions,lldpLocPortNum,lldpPortConfigEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_C,'lldpExtensions',_F,'lldpPortConfigEntry',_G,_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
lldpXHmMIB=ModuleIdentity((1,0,8802,1,1,2,1,5,32867))
if mibBuilder.loadTexts:lldpXHmMIB.setRevisions(('2008-09-12 12:00',))
class LldpXHmLocGMRPServiceReqSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_D,3)))
class LldpXHmLocIGMPVersionSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2)))
class LldpXHmLocPortSecModeSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_T,2),(_U,3),(_V,4),('multiClient',5)))
class LldpXHmLocPTPSupportSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3)))
class LldpXHmLocPTPStatusSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_a,0),(_b,1)))
class LldpXHmLocPTPv2DataTransferSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_D,4)))
class LldpXHmLocPTPv2DelayMechanismSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('p2p',1),('e2e',2),(_f,3),(_D,4)))
class LldpXHmRemGMRPServiceReqSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_D,3)))
class LldpXHmRemPTPv2DataTransferSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_D,4)))
class LldpXHmRemPTPv2DelayMechanismSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('p2p',1),('e2e',2),(_f,3),(_D,4)))
class LldpXHmRemPTPSupportSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3)))
class LldpXHmRemPTPStatusSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_a,0),(_b,1)))
class LldpXHmRemPortSecModeSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_T,2),(_U,3),(_V,4)))
class LldpXHmRemIGMPVersionSyntax(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2)))
_LldpXHmObjects_ObjectIdentity=ObjectIdentity
lldpXHmObjects=_LldpXHmObjects_ObjectIdentity((1,0,8802,1,1,2,1,5,32867,1))
_LldpXHmConfig_ObjectIdentity=ObjectIdentity
lldpXHmConfig=_LldpXHmConfig_ObjectIdentity((1,0,8802,1,1,2,1,5,32867,1,1))
_LldpXHmConfigGMRPTable_Object=MibTable
lldpXHmConfigGMRPTable=_LldpXHmConfigGMRPTable_Object((1,0,8802,1,1,2,1,5,32867,1,1,1))
if mibBuilder.loadTexts:lldpXHmConfigGMRPTable.setStatus(_A)
_LldpXHmConfigGMRPEntry_Object=MibTableRow
lldpXHmConfigGMRPEntry=_LldpXHmConfigGMRPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,1,1,1))
if mibBuilder.loadTexts:lldpXHmConfigGMRPEntry.setStatus(_A)
class _LldpXHmConfigGMRPTxEnable_Type(TruthValue):defaultValue=2
_LldpXHmConfigGMRPTxEnable_Type.__name__=_J
_LldpXHmConfigGMRPTxEnable_Object=MibTableColumn
lldpXHmConfigGMRPTxEnable=_LldpXHmConfigGMRPTxEnable_Object((1,0,8802,1,1,2,1,5,32867,1,1,1,1,1),_LldpXHmConfigGMRPTxEnable_Type())
lldpXHmConfigGMRPTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXHmConfigGMRPTxEnable.setStatus(_A)
_LldpXHmConfigIGMPTable_Object=MibTable
lldpXHmConfigIGMPTable=_LldpXHmConfigIGMPTable_Object((1,0,8802,1,1,2,1,5,32867,1,1,2))
if mibBuilder.loadTexts:lldpXHmConfigIGMPTable.setStatus(_A)
_LldpXHmConfigIGMPEntry_Object=MibTableRow
lldpXHmConfigIGMPEntry=_LldpXHmConfigIGMPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,1,2,1))
if mibBuilder.loadTexts:lldpXHmConfigIGMPEntry.setStatus(_A)
class _LldpXHmConfigIGMPTxEnable_Type(TruthValue):defaultValue=2
_LldpXHmConfigIGMPTxEnable_Type.__name__=_J
_LldpXHmConfigIGMPTxEnable_Object=MibTableColumn
lldpXHmConfigIGMPTxEnable=_LldpXHmConfigIGMPTxEnable_Object((1,0,8802,1,1,2,1,5,32867,1,1,2,1,1),_LldpXHmConfigIGMPTxEnable_Type())
lldpXHmConfigIGMPTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXHmConfigIGMPTxEnable.setStatus(_A)
_LldpXHmConfigPortSecTable_Object=MibTable
lldpXHmConfigPortSecTable=_LldpXHmConfigPortSecTable_Object((1,0,8802,1,1,2,1,5,32867,1,1,3))
if mibBuilder.loadTexts:lldpXHmConfigPortSecTable.setStatus(_A)
_LldpXHmConfigPortSecEntry_Object=MibTableRow
lldpXHmConfigPortSecEntry=_LldpXHmConfigPortSecEntry_Object((1,0,8802,1,1,2,1,5,32867,1,1,3,1))
if mibBuilder.loadTexts:lldpXHmConfigPortSecEntry.setStatus(_A)
class _LldpXHmConfigPortSecTxEnable_Type(TruthValue):defaultValue=2
_LldpXHmConfigPortSecTxEnable_Type.__name__=_J
_LldpXHmConfigPortSecTxEnable_Object=MibTableColumn
lldpXHmConfigPortSecTxEnable=_LldpXHmConfigPortSecTxEnable_Object((1,0,8802,1,1,2,1,5,32867,1,1,3,1,1),_LldpXHmConfigPortSecTxEnable_Type())
lldpXHmConfigPortSecTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXHmConfigPortSecTxEnable.setStatus(_A)
_LldpXHmConfigPTPTable_Object=MibTable
lldpXHmConfigPTPTable=_LldpXHmConfigPTPTable_Object((1,0,8802,1,1,2,1,5,32867,1,1,4))
if mibBuilder.loadTexts:lldpXHmConfigPTPTable.setStatus(_A)
_LldpXHmConfigPTPEntry_Object=MibTableRow
lldpXHmConfigPTPEntry=_LldpXHmConfigPTPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,1,4,1))
if mibBuilder.loadTexts:lldpXHmConfigPTPEntry.setStatus(_A)
class _LldpXHmConfigPTPTxEnable_Type(TruthValue):defaultValue=2
_LldpXHmConfigPTPTxEnable_Type.__name__=_J
_LldpXHmConfigPTPTxEnable_Object=MibTableColumn
lldpXHmConfigPTPTxEnable=_LldpXHmConfigPTPTxEnable_Object((1,0,8802,1,1,2,1,5,32867,1,1,4,1,1),_LldpXHmConfigPTPTxEnable_Type())
lldpXHmConfigPTPTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXHmConfigPTPTxEnable.setStatus(_A)
_LldpXHmLocalData_ObjectIdentity=ObjectIdentity
lldpXHmLocalData=_LldpXHmLocalData_ObjectIdentity((1,0,8802,1,1,2,1,5,32867,1,2))
_LldpXHmLocGMRPTable_Object=MibTable
lldpXHmLocGMRPTable=_LldpXHmLocGMRPTable_Object((1,0,8802,1,1,2,1,5,32867,1,2,1))
if mibBuilder.loadTexts:lldpXHmLocGMRPTable.setStatus(_A)
_LldpXHmLocGMRPEntry_Object=MibTableRow
lldpXHmLocGMRPEntry=_LldpXHmLocGMRPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,2,1,1))
lldpXHmLocGMRPEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXHmLocGMRPEntry.setStatus(_A)
_LldpXHmLocGMRPSupport_Type=TruthValue
_LldpXHmLocGMRPSupport_Object=MibTableColumn
lldpXHmLocGMRPSupport=_LldpXHmLocGMRPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,2,1,1,1),_LldpXHmLocGMRPSupport_Type())
lldpXHmLocGMRPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocGMRPSupport.setStatus(_A)
_LldpXHmLocGMRPStatus_Type=TruthValue
_LldpXHmLocGMRPStatus_Object=MibTableColumn
lldpXHmLocGMRPStatus=_LldpXHmLocGMRPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,2,1,1,2),_LldpXHmLocGMRPStatus_Type())
lldpXHmLocGMRPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocGMRPStatus.setStatus(_A)
_LldpXHmLocGMRPServiceReq_Type=LldpXHmLocGMRPServiceReqSyntax
_LldpXHmLocGMRPServiceReq_Object=MibTableColumn
lldpXHmLocGMRPServiceReq=_LldpXHmLocGMRPServiceReq_Object((1,0,8802,1,1,2,1,5,32867,1,2,1,1,3),_LldpXHmLocGMRPServiceReq_Type())
lldpXHmLocGMRPServiceReq.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocGMRPServiceReq.setStatus(_A)
_LldpXHmLocIGMPTable_Object=MibTable
lldpXHmLocIGMPTable=_LldpXHmLocIGMPTable_Object((1,0,8802,1,1,2,1,5,32867,1,2,2))
if mibBuilder.loadTexts:lldpXHmLocIGMPTable.setStatus(_A)
_LldpXHmLocIGMPEntry_Object=MibTableRow
lldpXHmLocIGMPEntry=_LldpXHmLocIGMPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,2,2,1))
lldpXHmLocIGMPEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXHmLocIGMPEntry.setStatus(_A)
_LldpXHmLocIGMPSupport_Type=TruthValue
_LldpXHmLocIGMPSupport_Object=MibTableColumn
lldpXHmLocIGMPSupport=_LldpXHmLocIGMPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,2,2,1,1),_LldpXHmLocIGMPSupport_Type())
lldpXHmLocIGMPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocIGMPSupport.setStatus(_A)
_LldpXHmLocIGMPStatus_Type=TruthValue
_LldpXHmLocIGMPStatus_Object=MibTableColumn
lldpXHmLocIGMPStatus=_LldpXHmLocIGMPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,2,2,1,2),_LldpXHmLocIGMPStatus_Type())
lldpXHmLocIGMPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocIGMPStatus.setStatus(_A)
_LldpXHmLocIGMPVersion_Type=LldpXHmLocIGMPVersionSyntax
_LldpXHmLocIGMPVersion_Object=MibTableColumn
lldpXHmLocIGMPVersion=_LldpXHmLocIGMPVersion_Object((1,0,8802,1,1,2,1,5,32867,1,2,2,1,3),_LldpXHmLocIGMPVersion_Type())
lldpXHmLocIGMPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocIGMPVersion.setStatus(_A)
_LldpXHmLocPortSecTable_Object=MibTable
lldpXHmLocPortSecTable=_LldpXHmLocPortSecTable_Object((1,0,8802,1,1,2,1,5,32867,1,2,3))
if mibBuilder.loadTexts:lldpXHmLocPortSecTable.setStatus(_A)
_LldpXHmLocPortSecEntry_Object=MibTableRow
lldpXHmLocPortSecEntry=_LldpXHmLocPortSecEntry_Object((1,0,8802,1,1,2,1,5,32867,1,2,3,1))
lldpXHmLocPortSecEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXHmLocPortSecEntry.setStatus(_A)
_LldpXHmLocPortSecSupport_Type=TruthValue
_LldpXHmLocPortSecSupport_Object=MibTableColumn
lldpXHmLocPortSecSupport=_LldpXHmLocPortSecSupport_Object((1,0,8802,1,1,2,1,5,32867,1,2,3,1,1),_LldpXHmLocPortSecSupport_Type())
lldpXHmLocPortSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPortSecSupport.setStatus(_A)
_LldpXHmLocPortSecStatus_Type=TruthValue
_LldpXHmLocPortSecStatus_Object=MibTableColumn
lldpXHmLocPortSecStatus=_LldpXHmLocPortSecStatus_Object((1,0,8802,1,1,2,1,5,32867,1,2,3,1,2),_LldpXHmLocPortSecStatus_Type())
lldpXHmLocPortSecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPortSecStatus.setStatus(_A)
_LldpXHmLocPortSecMode_Type=LldpXHmLocPortSecModeSyntax
_LldpXHmLocPortSecMode_Object=MibTableColumn
lldpXHmLocPortSecMode=_LldpXHmLocPortSecMode_Object((1,0,8802,1,1,2,1,5,32867,1,2,3,1,3),_LldpXHmLocPortSecMode_Type())
lldpXHmLocPortSecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPortSecMode.setStatus(_A)
_LldpXHmLocPTPTable_Object=MibTable
lldpXHmLocPTPTable=_LldpXHmLocPTPTable_Object((1,0,8802,1,1,2,1,5,32867,1,2,4))
if mibBuilder.loadTexts:lldpXHmLocPTPTable.setStatus(_A)
_LldpXHmLocPTPEntry_Object=MibTableRow
lldpXHmLocPTPEntry=_LldpXHmLocPTPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1))
lldpXHmLocPTPEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXHmLocPTPEntry.setStatus(_A)
_LldpXHmLocPTPSupport_Type=LldpXHmLocPTPSupportSyntax
_LldpXHmLocPTPSupport_Object=MibTableColumn
lldpXHmLocPTPSupport=_LldpXHmLocPTPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,1),_LldpXHmLocPTPSupport_Type())
lldpXHmLocPTPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPSupport.setStatus(_A)
_LldpXHmLocPTPStatus_Type=LldpXHmLocPTPStatusSyntax
_LldpXHmLocPTPStatus_Object=MibTableColumn
lldpXHmLocPTPStatus=_LldpXHmLocPTPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,2),_LldpXHmLocPTPStatus_Type())
lldpXHmLocPTPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPStatus.setStatus(_A)
class _LldpXHmLocPTPSyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_LldpXHmLocPTPSyncInterval_Type.__name__=_E
_LldpXHmLocPTPSyncInterval_Object=MibTableColumn
lldpXHmLocPTPSyncInterval=_LldpXHmLocPTPSyncInterval_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,3),_LldpXHmLocPTPSyncInterval_Type())
lldpXHmLocPTPSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPSyncInterval.setStatus(_A)
class _LldpXHmLocPTPv2AnnounceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_LldpXHmLocPTPv2AnnounceInterval_Type.__name__=_E
_LldpXHmLocPTPv2AnnounceInterval_Object=MibTableColumn
lldpXHmLocPTPv2AnnounceInterval=_LldpXHmLocPTPv2AnnounceInterval_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,4),_LldpXHmLocPTPv2AnnounceInterval_Type())
lldpXHmLocPTPv2AnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPv2AnnounceInterval.setStatus(_A)
_LldpXHmLocPTPv2DataTransfer_Type=LldpXHmLocPTPv2DataTransferSyntax
_LldpXHmLocPTPv2DataTransfer_Object=MibTableColumn
lldpXHmLocPTPv2DataTransfer=_LldpXHmLocPTPv2DataTransfer_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,5),_LldpXHmLocPTPv2DataTransfer_Type())
lldpXHmLocPTPv2DataTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPv2DataTransfer.setStatus(_A)
_LldpXHmLocPTPv2DelayMechanism_Type=LldpXHmLocPTPv2DelayMechanismSyntax
_LldpXHmLocPTPv2DelayMechanism_Object=MibTableColumn
lldpXHmLocPTPv2DelayMechanism=_LldpXHmLocPTPv2DelayMechanism_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,6),_LldpXHmLocPTPv2DelayMechanism_Type())
lldpXHmLocPTPv2DelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPv2DelayMechanism.setStatus(_A)
class _LldpXHmLocPTPClockValues_Type(Bits):namedValues=NamedValues(*(('slave',0),(_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_LldpXHmLocPTPClockValues_Type.__name__=_N
_LldpXHmLocPTPClockValues_Object=MibTableColumn
lldpXHmLocPTPClockValues=_LldpXHmLocPTPClockValues_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,7),_LldpXHmLocPTPClockValues_Type())
lldpXHmLocPTPClockValues.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPClockValues.setStatus(_A)
class _LldpXHmLocPTPv2SubdomainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LldpXHmLocPTPv2SubdomainNumber_Type.__name__=_E
_LldpXHmLocPTPv2SubdomainNumber_Object=MibTableColumn
lldpXHmLocPTPv2SubdomainNumber=_LldpXHmLocPTPv2SubdomainNumber_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,8),_LldpXHmLocPTPv2SubdomainNumber_Type())
lldpXHmLocPTPv2SubdomainNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPv2SubdomainNumber.setStatus(_A)
class _LldpXHmLocPTPv1SubdomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LldpXHmLocPTPv1SubdomainName_Type.__name__=_M
_LldpXHmLocPTPv1SubdomainName_Object=MibTableColumn
lldpXHmLocPTPv1SubdomainName=_LldpXHmLocPTPv1SubdomainName_Object((1,0,8802,1,1,2,1,5,32867,1,2,4,1,9),_LldpXHmLocPTPv1SubdomainName_Type())
lldpXHmLocPTPv1SubdomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmLocPTPv1SubdomainName.setStatus(_A)
_LldpXHmRemoteData_ObjectIdentity=ObjectIdentity
lldpXHmRemoteData=_LldpXHmRemoteData_ObjectIdentity((1,0,8802,1,1,2,1,5,32867,1,3))
_LldpXHmRemGMRPTable_Object=MibTable
lldpXHmRemGMRPTable=_LldpXHmRemGMRPTable_Object((1,0,8802,1,1,2,1,5,32867,1,3,1))
if mibBuilder.loadTexts:lldpXHmRemGMRPTable.setStatus(_A)
_LldpXHmRemGMRPEntry_Object=MibTableRow
lldpXHmRemGMRPEntry=_LldpXHmRemGMRPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,3,1,1))
lldpXHmRemGMRPEntry.setIndexNames((0,_C,_I),(0,_C,_H),(0,_C,_G))
if mibBuilder.loadTexts:lldpXHmRemGMRPEntry.setStatus(_A)
_LldpXHmRemGMRPSupport_Type=TruthValue
_LldpXHmRemGMRPSupport_Object=MibTableColumn
lldpXHmRemGMRPSupport=_LldpXHmRemGMRPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,3,1,1,1),_LldpXHmRemGMRPSupport_Type())
lldpXHmRemGMRPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemGMRPSupport.setStatus(_A)
_LldpXHmRemGMRPStatus_Type=TruthValue
_LldpXHmRemGMRPStatus_Object=MibTableColumn
lldpXHmRemGMRPStatus=_LldpXHmRemGMRPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,3,1,1,2),_LldpXHmRemGMRPStatus_Type())
lldpXHmRemGMRPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemGMRPStatus.setStatus(_A)
_LldpXHmRemGMRPServiceReq_Type=LldpXHmRemGMRPServiceReqSyntax
_LldpXHmRemGMRPServiceReq_Object=MibTableColumn
lldpXHmRemGMRPServiceReq=_LldpXHmRemGMRPServiceReq_Object((1,0,8802,1,1,2,1,5,32867,1,3,1,1,3),_LldpXHmRemGMRPServiceReq_Type())
lldpXHmRemGMRPServiceReq.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemGMRPServiceReq.setStatus(_A)
_LldpXHmRemIGMPTable_Object=MibTable
lldpXHmRemIGMPTable=_LldpXHmRemIGMPTable_Object((1,0,8802,1,1,2,1,5,32867,1,3,2))
if mibBuilder.loadTexts:lldpXHmRemIGMPTable.setStatus(_A)
_LldpXHmRemIGMPEntry_Object=MibTableRow
lldpXHmRemIGMPEntry=_LldpXHmRemIGMPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,3,2,1))
lldpXHmRemIGMPEntry.setIndexNames((0,_C,_I),(0,_C,_H),(0,_C,_G))
if mibBuilder.loadTexts:lldpXHmRemIGMPEntry.setStatus(_A)
_LldpXHmRemIGMPSupport_Type=TruthValue
_LldpXHmRemIGMPSupport_Object=MibTableColumn
lldpXHmRemIGMPSupport=_LldpXHmRemIGMPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,3,2,1,1),_LldpXHmRemIGMPSupport_Type())
lldpXHmRemIGMPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemIGMPSupport.setStatus(_A)
_LldpXHmRemIGMPStatus_Type=TruthValue
_LldpXHmRemIGMPStatus_Object=MibTableColumn
lldpXHmRemIGMPStatus=_LldpXHmRemIGMPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,3,2,1,2),_LldpXHmRemIGMPStatus_Type())
lldpXHmRemIGMPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemIGMPStatus.setStatus(_A)
_LldpXHmRemIGMPVersion_Type=LldpXHmRemIGMPVersionSyntax
_LldpXHmRemIGMPVersion_Object=MibTableColumn
lldpXHmRemIGMPVersion=_LldpXHmRemIGMPVersion_Object((1,0,8802,1,1,2,1,5,32867,1,3,2,1,3),_LldpXHmRemIGMPVersion_Type())
lldpXHmRemIGMPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemIGMPVersion.setStatus(_A)
_LldpXHmRemPortSecTable_Object=MibTable
lldpXHmRemPortSecTable=_LldpXHmRemPortSecTable_Object((1,0,8802,1,1,2,1,5,32867,1,3,3))
if mibBuilder.loadTexts:lldpXHmRemPortSecTable.setStatus(_A)
_LldpXHmRemPortSecEntry_Object=MibTableRow
lldpXHmRemPortSecEntry=_LldpXHmRemPortSecEntry_Object((1,0,8802,1,1,2,1,5,32867,1,3,3,1))
lldpXHmRemPortSecEntry.setIndexNames((0,_C,_I),(0,_C,_H),(0,_C,_G))
if mibBuilder.loadTexts:lldpXHmRemPortSecEntry.setStatus(_A)
_LldpXHmRemPortSecSupport_Type=TruthValue
_LldpXHmRemPortSecSupport_Object=MibTableColumn
lldpXHmRemPortSecSupport=_LldpXHmRemPortSecSupport_Object((1,0,8802,1,1,2,1,5,32867,1,3,3,1,1),_LldpXHmRemPortSecSupport_Type())
lldpXHmRemPortSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPortSecSupport.setStatus(_A)
_LldpXHmRemPortSecStatus_Type=TruthValue
_LldpXHmRemPortSecStatus_Object=MibTableColumn
lldpXHmRemPortSecStatus=_LldpXHmRemPortSecStatus_Object((1,0,8802,1,1,2,1,5,32867,1,3,3,1,2),_LldpXHmRemPortSecStatus_Type())
lldpXHmRemPortSecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPortSecStatus.setStatus(_A)
_LldpXHmRemPortSecMode_Type=LldpXHmRemPortSecModeSyntax
_LldpXHmRemPortSecMode_Object=MibTableColumn
lldpXHmRemPortSecMode=_LldpXHmRemPortSecMode_Object((1,0,8802,1,1,2,1,5,32867,1,3,3,1,3),_LldpXHmRemPortSecMode_Type())
lldpXHmRemPortSecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPortSecMode.setStatus(_A)
_LldpXHmRemPTPTable_Object=MibTable
lldpXHmRemPTPTable=_LldpXHmRemPTPTable_Object((1,0,8802,1,1,2,1,5,32867,1,3,4))
if mibBuilder.loadTexts:lldpXHmRemPTPTable.setStatus(_A)
_LldpXHmRemPTPEntry_Object=MibTableRow
lldpXHmRemPTPEntry=_LldpXHmRemPTPEntry_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1))
lldpXHmRemPTPEntry.setIndexNames((0,_C,_I),(0,_C,_H),(0,_C,_G))
if mibBuilder.loadTexts:lldpXHmRemPTPEntry.setStatus(_A)
_LldpXHmRemPTPSupport_Type=LldpXHmRemPTPSupportSyntax
_LldpXHmRemPTPSupport_Object=MibTableColumn
lldpXHmRemPTPSupport=_LldpXHmRemPTPSupport_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,1),_LldpXHmRemPTPSupport_Type())
lldpXHmRemPTPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPSupport.setStatus(_A)
_LldpXHmRemPTPStatus_Type=LldpXHmRemPTPStatusSyntax
_LldpXHmRemPTPStatus_Object=MibTableColumn
lldpXHmRemPTPStatus=_LldpXHmRemPTPStatus_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,2),_LldpXHmRemPTPStatus_Type())
lldpXHmRemPTPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPStatus.setStatus(_A)
class _LldpXHmRemPTPSyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_LldpXHmRemPTPSyncInterval_Type.__name__=_E
_LldpXHmRemPTPSyncInterval_Object=MibTableColumn
lldpXHmRemPTPSyncInterval=_LldpXHmRemPTPSyncInterval_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,3),_LldpXHmRemPTPSyncInterval_Type())
lldpXHmRemPTPSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPSyncInterval.setStatus(_A)
class _LldpXHmRemPTPv2AnnounceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_LldpXHmRemPTPv2AnnounceInterval_Type.__name__=_E
_LldpXHmRemPTPv2AnnounceInterval_Object=MibTableColumn
lldpXHmRemPTPv2AnnounceInterval=_LldpXHmRemPTPv2AnnounceInterval_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,4),_LldpXHmRemPTPv2AnnounceInterval_Type())
lldpXHmRemPTPv2AnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPv2AnnounceInterval.setStatus(_A)
_LldpXHmRemPTPv2DataTransfer_Type=LldpXHmRemPTPv2DataTransferSyntax
_LldpXHmRemPTPv2DataTransfer_Object=MibTableColumn
lldpXHmRemPTPv2DataTransfer=_LldpXHmRemPTPv2DataTransfer_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,5),_LldpXHmRemPTPv2DataTransfer_Type())
lldpXHmRemPTPv2DataTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPv2DataTransfer.setStatus(_A)
_LldpXHmRemPTPv2DelayMechanism_Type=LldpXHmRemPTPv2DelayMechanismSyntax
_LldpXHmRemPTPv2DelayMechanism_Object=MibTableColumn
lldpXHmRemPTPv2DelayMechanism=_LldpXHmRemPTPv2DelayMechanism_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,6),_LldpXHmRemPTPv2DelayMechanism_Type())
lldpXHmRemPTPv2DelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPv2DelayMechanism.setStatus(_A)
class _LldpXHmRemPTPClockValues_Type(Bits):namedValues=NamedValues(*(('slave',0),(_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_LldpXHmRemPTPClockValues_Type.__name__=_N
_LldpXHmRemPTPClockValues_Object=MibTableColumn
lldpXHmRemPTPClockValues=_LldpXHmRemPTPClockValues_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,7),_LldpXHmRemPTPClockValues_Type())
lldpXHmRemPTPClockValues.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPClockValues.setStatus(_A)
class _LldpXHmRemPTPv2SubdomainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LldpXHmRemPTPv2SubdomainNumber_Type.__name__=_E
_LldpXHmRemPTPv2SubdomainNumber_Object=MibTableColumn
lldpXHmRemPTPv2SubdomainNumber=_LldpXHmRemPTPv2SubdomainNumber_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,8),_LldpXHmRemPTPv2SubdomainNumber_Type())
lldpXHmRemPTPv2SubdomainNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPv2SubdomainNumber.setStatus(_A)
class _LldpXHmRemPTPv1SubdomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LldpXHmRemPTPv1SubdomainName_Type.__name__=_M
_LldpXHmRemPTPv1SubdomainName_Object=MibTableColumn
lldpXHmRemPTPv1SubdomainName=_LldpXHmRemPTPv1SubdomainName_Object((1,0,8802,1,1,2,1,5,32867,1,3,4,1,9),_LldpXHmRemPTPv1SubdomainName_Type())
lldpXHmRemPTPv1SubdomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpXHmRemPTPv1SubdomainName.setStatus(_A)
lldpPortConfigEntry.registerAugmentions((_K,_m))
lldpXHmConfigGMRPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions((_K,_n))
lldpXHmConfigIGMPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions((_K,_o))
lldpXHmConfigPortSecEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions((_K,_p))
lldpXHmConfigPTPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_K,**{'LldpXHmLocGMRPServiceReqSyntax':LldpXHmLocGMRPServiceReqSyntax,'LldpXHmLocIGMPVersionSyntax':LldpXHmLocIGMPVersionSyntax,'LldpXHmLocPortSecModeSyntax':LldpXHmLocPortSecModeSyntax,'LldpXHmLocPTPSupportSyntax':LldpXHmLocPTPSupportSyntax,'LldpXHmLocPTPStatusSyntax':LldpXHmLocPTPStatusSyntax,'LldpXHmLocPTPv2DataTransferSyntax':LldpXHmLocPTPv2DataTransferSyntax,'LldpXHmLocPTPv2DelayMechanismSyntax':LldpXHmLocPTPv2DelayMechanismSyntax,'LldpXHmRemGMRPServiceReqSyntax':LldpXHmRemGMRPServiceReqSyntax,'LldpXHmRemPTPv2DataTransferSyntax':LldpXHmRemPTPv2DataTransferSyntax,'LldpXHmRemPTPv2DelayMechanismSyntax':LldpXHmRemPTPv2DelayMechanismSyntax,'LldpXHmRemPTPSupportSyntax':LldpXHmRemPTPSupportSyntax,'LldpXHmRemPTPStatusSyntax':LldpXHmRemPTPStatusSyntax,'LldpXHmRemPortSecModeSyntax':LldpXHmRemPortSecModeSyntax,'LldpXHmRemIGMPVersionSyntax':LldpXHmRemIGMPVersionSyntax,'lldpXHmMIB':lldpXHmMIB,'lldpXHmObjects':lldpXHmObjects,'lldpXHmConfig':lldpXHmConfig,'lldpXHmConfigGMRPTable':lldpXHmConfigGMRPTable,_m:lldpXHmConfigGMRPEntry,'lldpXHmConfigGMRPTxEnable':lldpXHmConfigGMRPTxEnable,'lldpXHmConfigIGMPTable':lldpXHmConfigIGMPTable,_n:lldpXHmConfigIGMPEntry,'lldpXHmConfigIGMPTxEnable':lldpXHmConfigIGMPTxEnable,'lldpXHmConfigPortSecTable':lldpXHmConfigPortSecTable,_o:lldpXHmConfigPortSecEntry,'lldpXHmConfigPortSecTxEnable':lldpXHmConfigPortSecTxEnable,'lldpXHmConfigPTPTable':lldpXHmConfigPTPTable,_p:lldpXHmConfigPTPEntry,'lldpXHmConfigPTPTxEnable':lldpXHmConfigPTPTxEnable,'lldpXHmLocalData':lldpXHmLocalData,'lldpXHmLocGMRPTable':lldpXHmLocGMRPTable,'lldpXHmLocGMRPEntry':lldpXHmLocGMRPEntry,'lldpXHmLocGMRPSupport':lldpXHmLocGMRPSupport,'lldpXHmLocGMRPStatus':lldpXHmLocGMRPStatus,'lldpXHmLocGMRPServiceReq':lldpXHmLocGMRPServiceReq,'lldpXHmLocIGMPTable':lldpXHmLocIGMPTable,'lldpXHmLocIGMPEntry':lldpXHmLocIGMPEntry,'lldpXHmLocIGMPSupport':lldpXHmLocIGMPSupport,'lldpXHmLocIGMPStatus':lldpXHmLocIGMPStatus,'lldpXHmLocIGMPVersion':lldpXHmLocIGMPVersion,'lldpXHmLocPortSecTable':lldpXHmLocPortSecTable,'lldpXHmLocPortSecEntry':lldpXHmLocPortSecEntry,'lldpXHmLocPortSecSupport':lldpXHmLocPortSecSupport,'lldpXHmLocPortSecStatus':lldpXHmLocPortSecStatus,'lldpXHmLocPortSecMode':lldpXHmLocPortSecMode,'lldpXHmLocPTPTable':lldpXHmLocPTPTable,'lldpXHmLocPTPEntry':lldpXHmLocPTPEntry,'lldpXHmLocPTPSupport':lldpXHmLocPTPSupport,'lldpXHmLocPTPStatus':lldpXHmLocPTPStatus,'lldpXHmLocPTPSyncInterval':lldpXHmLocPTPSyncInterval,'lldpXHmLocPTPv2AnnounceInterval':lldpXHmLocPTPv2AnnounceInterval,'lldpXHmLocPTPv2DataTransfer':lldpXHmLocPTPv2DataTransfer,'lldpXHmLocPTPv2DelayMechanism':lldpXHmLocPTPv2DelayMechanism,'lldpXHmLocPTPClockValues':lldpXHmLocPTPClockValues,'lldpXHmLocPTPv2SubdomainNumber':lldpXHmLocPTPv2SubdomainNumber,'lldpXHmLocPTPv1SubdomainName':lldpXHmLocPTPv1SubdomainName,'lldpXHmRemoteData':lldpXHmRemoteData,'lldpXHmRemGMRPTable':lldpXHmRemGMRPTable,'lldpXHmRemGMRPEntry':lldpXHmRemGMRPEntry,'lldpXHmRemGMRPSupport':lldpXHmRemGMRPSupport,'lldpXHmRemGMRPStatus':lldpXHmRemGMRPStatus,'lldpXHmRemGMRPServiceReq':lldpXHmRemGMRPServiceReq,'lldpXHmRemIGMPTable':lldpXHmRemIGMPTable,'lldpXHmRemIGMPEntry':lldpXHmRemIGMPEntry,'lldpXHmRemIGMPSupport':lldpXHmRemIGMPSupport,'lldpXHmRemIGMPStatus':lldpXHmRemIGMPStatus,'lldpXHmRemIGMPVersion':lldpXHmRemIGMPVersion,'lldpXHmRemPortSecTable':lldpXHmRemPortSecTable,'lldpXHmRemPortSecEntry':lldpXHmRemPortSecEntry,'lldpXHmRemPortSecSupport':lldpXHmRemPortSecSupport,'lldpXHmRemPortSecStatus':lldpXHmRemPortSecStatus,'lldpXHmRemPortSecMode':lldpXHmRemPortSecMode,'lldpXHmRemPTPTable':lldpXHmRemPTPTable,'lldpXHmRemPTPEntry':lldpXHmRemPTPEntry,'lldpXHmRemPTPSupport':lldpXHmRemPTPSupport,'lldpXHmRemPTPStatus':lldpXHmRemPTPStatus,'lldpXHmRemPTPSyncInterval':lldpXHmRemPTPSyncInterval,'lldpXHmRemPTPv2AnnounceInterval':lldpXHmRemPTPv2AnnounceInterval,'lldpXHmRemPTPv2DataTransfer':lldpXHmRemPTPv2DataTransfer,'lldpXHmRemPTPv2DelayMechanism':lldpXHmRemPTPv2DelayMechanism,'lldpXHmRemPTPClockValues':lldpXHmRemPTPClockValues,'lldpXHmRemPTPv2SubdomainNumber':lldpXHmRemPTPv2SubdomainNumber,'lldpXHmRemPTPv1SubdomainName':lldpXHmRemPTPv1SubdomainName})