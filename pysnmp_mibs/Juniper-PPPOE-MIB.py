_An='juniPPPoEServiceNameTableGroup1'
_Am='juniPPPoEGroup9'
_Al='juniPPPoEGroup8'
_Ak='juniPPPoEGroup7'
_Aj='juniPPPoEGroup6'
_Ai='juniPPPoEGroup5'
_Ah='juniPPPoEGroup4'
_Ag='juniPPPoEGroup3'
_Af='juniPPPoESubIfGroup'
_Ae='juniPPPoEGroup'
_Ad='juniPPPoEServiceNameTableUnknownAction'
_Ac='juniPPPoEMaxSessionVsa'
_Ab='juniPPPoEIfLockoutNextTime'
_Aa='juniPPPoEIfLockoutElapsedTime'
_AZ='juniPPPoEIfLockoutTime'
_AY='juniPPPoESummarySubIfLowerLayerDown'
_AX='juniPPPoESummarySubIfNotPresent'
_AW='juniPPPoESummarySubIfOperDown'
_AV='juniPPPoESummarySubIfOperUp'
_AU='juniPPPoESummarySubIfAdminDown'
_AT='juniPPPoESummarySubIfAdminUp'
_AS='juniPPPoESummarySubInterfaceCount'
_AR='juniPPPoESummaryMajorIfLowerLayerDown'
_AQ='juniPPPoESummaryMajorIfNotPresent'
_AP='juniPPPoESummaryMajorIfOperDown'
_AO='juniPPPoESummaryMajorIfOperUp'
_AN='juniPPPoESummaryMajorIfAdminDown'
_AM='juniPPPoESummaryMajorIfAdminUp'
_AL='juniPPPoEMajorInterfaceCount'
_AK='juniPPPoESubIfMotm'
_AJ='juniPPPoESubIfUrl'
_AI='juniPPPoEProfileMotm'
_AH='juniPPPoEProfileUrl'
_AG='juniPPPoEProfileRowStatus'
_AF='juniPPPoEServiceName'
_AE='juniPPPoEProfileIndex'
_AD='juniPPPoESubIfIndex'
_AC='juniPPPoEIfLockoutClientAddress'
_AB='juniPPPoEGroup10'
_AA='juniPPPoEProfileGroup'
_A9='juniPPPoEIfLockoutMax'
_A8='juniPPPoEIfLockoutMin'
_A7='juniPPPoEServiceNameRowStatus'
_A6='juniPPPoEServiceNameAction'
_A5='juniPPPoEServiceNameTableRowStatus'
_A4='juniPPPoEServiceNameTableEmptyAction'
_A3='juniPPPoEServiceNameTableName'
_A2='juniPPPoEServiceNameTableNextIndex'
_A1='juniPPPoESubIfSessionId'
_A0='juniPPPoESubIfId'
_z='juniPPPoESubIfLowerIfIndex'
_y='juniPPPoESubIfRowStatus'
_x='juniPPPoESubIfNextIfIndex'
_w='juniPPPoEServiceNameTableIndex'
_v='juniPPPoELockoutTableGroup'
_u='juniPPPoEGroup2'
_t='juniPPPoEIfMtu'
_s='juniPPPoEIfPadrRemoteCircuitIdCapture'
_r='not-accessible'
_q='read-write'
_p='JuniEnable'
_o='juniPPPoEServiceNameTableGroup'
_n='juniPPPoEIfStatsRxInvPadRSession'
_m='juniPPPoEIfStatsRxInvPadISession'
_l='juniPPPoEIfStatsRxInvLength'
_k='juniPPPoEIfStatsRxInvTagLength'
_j='juniPPPoEIfServiceNameTable'
_i='juniPPPoEIfStatsRxInvSession'
_h='juniPPPoEIfStatsTxPADN'
_g='deprecated'
_f='juniPPPoEIfAutoconfig'
_e='juniPPPoEIfPADIFlag'
_d='juniPPPoEIfDupProtect'
_c='juniPPPoEIfAcName'
_b='DisplayString'
_a='juniPPPoEGlobalMotm'
_Z='juniPPPoEIfStatsTxPADM'
_Y='juniPPPoEIfStatsRxInsufficientResources'
_X='juniPPPoEIfStatsRxInvPackets'
_W='juniPPPoEIfStatsRxInvTypes'
_V='juniPPPoEIfStatsRxInvTags'
_U='juniPPPoEIfStatsRxInvCode'
_T='juniPPPoEIfStatsRxInvVersion'
_S='juniPPPoEIfStatsTxPADT'
_R='juniPPPoEIfStatsRxPADT'
_Q='juniPPPoEIfStatsTxPADS'
_P='juniPPPoEIfStatsRxPADR'
_O='juniPPPoEIfStatsTxPADO'
_N='juniPPPoEIfStatsRxPADI'
_M='juniPPPoEIfLowerIfIndex'
_L='juniPPPoEIfRowStatus'
_K='juniPPPoEIfMaxNumSessions'
_J='juniPPPoENextIfIndex'
_I='Integer32'
_H='juniPPPoESummaryGroup'
_G='juniPPPoESubIfGroup2'
_F='juniPPPoEIfIfIndex'
_E='obsolete'
_D='read-create'
_C='read-only'
_B='current'
_A='Juniper-PPPOE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,JuniNextIfIndex=mibBuilder.importSymbols('Juniper-TC',_p,'JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
juniPPPoEMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,18))
if mibBuilder.loadTexts:juniPPPoEMIB.setRevisions(('2008-11-27 10:23','2008-06-18 09:42','2005-08-03 20:58','2005-05-18 12:01','2004-06-09 20:58','2003-03-10 18:30','2002-10-02 20:12','2002-10-01 18:27','2002-08-16 21:46','2001-06-19 14:27','2001-03-21 15:00','2001-02-12 00:00','2000-10-25 00:00','1999-05-13 00:00'))
class JuniPPPoEServiceNameAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('drop',0),('terminate',1)))
_JuniPPPoEObjects_ObjectIdentity=ObjectIdentity
juniPPPoEObjects=_JuniPPPoEObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1))
_JuniPPPoEIfLayer_ObjectIdentity=ObjectIdentity
juniPPPoEIfLayer=_JuniPPPoEIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,1))
_JuniPPPoENextIfIndex_Type=JuniNextIfIndex
_JuniPPPoENextIfIndex_Object=MibScalar
juniPPPoENextIfIndex=_JuniPPPoENextIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,1,1),_JuniPPPoENextIfIndex_Type())
juniPPPoENextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoENextIfIndex.setStatus(_B)
_JuniPPPoEIfTable_Object=MibTable
juniPPPoEIfTable=_JuniPPPoEIfTable_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2))
if mibBuilder.loadTexts:juniPPPoEIfTable.setStatus(_B)
_JuniPPPoEIfEntry_Object=MibTableRow
juniPPPoEIfEntry=_JuniPPPoEIfEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1))
juniPPPoEIfEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:juniPPPoEIfEntry.setStatus(_B)
_JuniPPPoEIfIfIndex_Type=InterfaceIndex
_JuniPPPoEIfIfIndex_Object=MibTableColumn
juniPPPoEIfIfIndex=_JuniPPPoEIfIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,1),_JuniPPPoEIfIfIndex_Type())
juniPPPoEIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfIfIndex.setStatus(_B)
class _JuniPPPoEIfMaxNumSessions_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65335))
_JuniPPPoEIfMaxNumSessions_Type.__name__=_I
_JuniPPPoEIfMaxNumSessions_Object=MibTableColumn
juniPPPoEIfMaxNumSessions=_JuniPPPoEIfMaxNumSessions_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,2),_JuniPPPoEIfMaxNumSessions_Type())
juniPPPoEIfMaxNumSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfMaxNumSessions.setStatus(_B)
_JuniPPPoEIfRowStatus_Type=RowStatus
_JuniPPPoEIfRowStatus_Object=MibTableColumn
juniPPPoEIfRowStatus=_JuniPPPoEIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,3),_JuniPPPoEIfRowStatus_Type())
juniPPPoEIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfRowStatus.setStatus(_B)
_JuniPPPoEIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniPPPoEIfLowerIfIndex_Object=MibTableColumn
juniPPPoEIfLowerIfIndex=_JuniPPPoEIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,4),_JuniPPPoEIfLowerIfIndex_Type())
juniPPPoEIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfLowerIfIndex.setStatus(_B)
class _JuniPPPoEIfAcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniPPPoEIfAcName_Type.__name__=_b
_JuniPPPoEIfAcName_Object=MibTableColumn
juniPPPoEIfAcName=_JuniPPPoEIfAcName_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,5),_JuniPPPoEIfAcName_Type())
juniPPPoEIfAcName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfAcName.setStatus(_B)
class _JuniPPPoEIfDupProtect_Type(JuniEnable):defaultValue=0
_JuniPPPoEIfDupProtect_Type.__name__=_p
_JuniPPPoEIfDupProtect_Object=MibTableColumn
juniPPPoEIfDupProtect=_JuniPPPoEIfDupProtect_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,6),_JuniPPPoEIfDupProtect_Type())
juniPPPoEIfDupProtect.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfDupProtect.setStatus(_B)
class _JuniPPPoEIfPADIFlag_Type(JuniEnable):defaultValue=0
_JuniPPPoEIfPADIFlag_Type.__name__=_p
_JuniPPPoEIfPADIFlag_Object=MibTableColumn
juniPPPoEIfPADIFlag=_JuniPPPoEIfPADIFlag_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,7),_JuniPPPoEIfPADIFlag_Type())
juniPPPoEIfPADIFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfPADIFlag.setStatus(_B)
class _JuniPPPoEIfAutoconfig_Type(JuniEnable):defaultValue=0
_JuniPPPoEIfAutoconfig_Type.__name__=_p
_JuniPPPoEIfAutoconfig_Object=MibTableColumn
juniPPPoEIfAutoconfig=_JuniPPPoEIfAutoconfig_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,8),_JuniPPPoEIfAutoconfig_Type())
juniPPPoEIfAutoconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfAutoconfig.setStatus(_B)
_JuniPPPoEIfServiceNameTable_Type=Unsigned32
_JuniPPPoEIfServiceNameTable_Object=MibTableColumn
juniPPPoEIfServiceNameTable=_JuniPPPoEIfServiceNameTable_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,9),_JuniPPPoEIfServiceNameTable_Type())
juniPPPoEIfServiceNameTable.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfServiceNameTable.setStatus(_B)
class _JuniPPPoEIfPadrRemoteCircuitIdCapture_Type(JuniEnable):defaultValue=0
_JuniPPPoEIfPadrRemoteCircuitIdCapture_Type.__name__=_p
_JuniPPPoEIfPadrRemoteCircuitIdCapture_Object=MibTableColumn
juniPPPoEIfPadrRemoteCircuitIdCapture=_JuniPPPoEIfPadrRemoteCircuitIdCapture_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,10),_JuniPPPoEIfPadrRemoteCircuitIdCapture_Type())
juniPPPoEIfPadrRemoteCircuitIdCapture.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEIfPadrRemoteCircuitIdCapture.setStatus(_B)
class _JuniPPPoEIfMtu_Type(Integer32):defaultValue=1494;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(66,65535))
_JuniPPPoEIfMtu_Type.__name__=_I
_JuniPPPoEIfMtu_Object=MibTableColumn
juniPPPoEIfMtu=_JuniPPPoEIfMtu_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,11),_JuniPPPoEIfMtu_Type())
juniPPPoEIfMtu.setMaxAccess(_q)
if mibBuilder.loadTexts:juniPPPoEIfMtu.setStatus(_B)
class _JuniPPPoEIfLockoutMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniPPPoEIfLockoutMin_Type.__name__=_I
_JuniPPPoEIfLockoutMin_Object=MibTableColumn
juniPPPoEIfLockoutMin=_JuniPPPoEIfLockoutMin_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,12),_JuniPPPoEIfLockoutMin_Type())
juniPPPoEIfLockoutMin.setMaxAccess(_q)
if mibBuilder.loadTexts:juniPPPoEIfLockoutMin.setStatus(_B)
class _JuniPPPoEIfLockoutMax_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniPPPoEIfLockoutMax_Type.__name__=_I
_JuniPPPoEIfLockoutMax_Object=MibTableColumn
juniPPPoEIfLockoutMax=_JuniPPPoEIfLockoutMax_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,13),_JuniPPPoEIfLockoutMax_Type())
juniPPPoEIfLockoutMax.setMaxAccess(_q)
if mibBuilder.loadTexts:juniPPPoEIfLockoutMax.setStatus(_B)
class _JuniPPPoEMaxSessionVsa_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('override',1),('ignore',2)))
_JuniPPPoEMaxSessionVsa_Type.__name__=_I
_JuniPPPoEMaxSessionVsa_Object=MibTableColumn
juniPPPoEMaxSessionVsa=_JuniPPPoEMaxSessionVsa_Object((1,3,6,1,4,1,4874,2,2,18,1,1,2,1,14),_JuniPPPoEMaxSessionVsa_Type())
juniPPPoEMaxSessionVsa.setMaxAccess(_q)
if mibBuilder.loadTexts:juniPPPoEMaxSessionVsa.setStatus(_B)
_JuniPPPoEIfStatsTable_Object=MibTable
juniPPPoEIfStatsTable=_JuniPPPoEIfStatsTable_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3))
if mibBuilder.loadTexts:juniPPPoEIfStatsTable.setStatus(_B)
_JuniPPPoEIfStatsEntry_Object=MibTableRow
juniPPPoEIfStatsEntry=_JuniPPPoEIfStatsEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1))
juniPPPoEIfStatsEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:juniPPPoEIfStatsEntry.setStatus(_B)
_JuniPPPoEIfStatsRxPADI_Type=Counter32
_JuniPPPoEIfStatsRxPADI_Object=MibTableColumn
juniPPPoEIfStatsRxPADI=_JuniPPPoEIfStatsRxPADI_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,1),_JuniPPPoEIfStatsRxPADI_Type())
juniPPPoEIfStatsRxPADI.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxPADI.setStatus(_B)
_JuniPPPoEIfStatsTxPADO_Type=Counter32
_JuniPPPoEIfStatsTxPADO_Object=MibTableColumn
juniPPPoEIfStatsTxPADO=_JuniPPPoEIfStatsTxPADO_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,2),_JuniPPPoEIfStatsTxPADO_Type())
juniPPPoEIfStatsTxPADO.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsTxPADO.setStatus(_B)
_JuniPPPoEIfStatsRxPADR_Type=Counter32
_JuniPPPoEIfStatsRxPADR_Object=MibTableColumn
juniPPPoEIfStatsRxPADR=_JuniPPPoEIfStatsRxPADR_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,3),_JuniPPPoEIfStatsRxPADR_Type())
juniPPPoEIfStatsRxPADR.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxPADR.setStatus(_B)
_JuniPPPoEIfStatsTxPADS_Type=Counter32
_JuniPPPoEIfStatsTxPADS_Object=MibTableColumn
juniPPPoEIfStatsTxPADS=_JuniPPPoEIfStatsTxPADS_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,4),_JuniPPPoEIfStatsTxPADS_Type())
juniPPPoEIfStatsTxPADS.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsTxPADS.setStatus(_B)
_JuniPPPoEIfStatsRxPADT_Type=Counter32
_JuniPPPoEIfStatsRxPADT_Object=MibTableColumn
juniPPPoEIfStatsRxPADT=_JuniPPPoEIfStatsRxPADT_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,5),_JuniPPPoEIfStatsRxPADT_Type())
juniPPPoEIfStatsRxPADT.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxPADT.setStatus(_B)
_JuniPPPoEIfStatsTxPADT_Type=Counter32
_JuniPPPoEIfStatsTxPADT_Object=MibTableColumn
juniPPPoEIfStatsTxPADT=_JuniPPPoEIfStatsTxPADT_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,6),_JuniPPPoEIfStatsTxPADT_Type())
juniPPPoEIfStatsTxPADT.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsTxPADT.setStatus(_B)
_JuniPPPoEIfStatsRxInvVersion_Type=Counter32
_JuniPPPoEIfStatsRxInvVersion_Object=MibTableColumn
juniPPPoEIfStatsRxInvVersion=_JuniPPPoEIfStatsRxInvVersion_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,7),_JuniPPPoEIfStatsRxInvVersion_Type())
juniPPPoEIfStatsRxInvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvVersion.setStatus(_B)
_JuniPPPoEIfStatsRxInvCode_Type=Counter32
_JuniPPPoEIfStatsRxInvCode_Object=MibTableColumn
juniPPPoEIfStatsRxInvCode=_JuniPPPoEIfStatsRxInvCode_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,8),_JuniPPPoEIfStatsRxInvCode_Type())
juniPPPoEIfStatsRxInvCode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvCode.setStatus(_B)
_JuniPPPoEIfStatsRxInvTags_Type=Counter32
_JuniPPPoEIfStatsRxInvTags_Object=MibTableColumn
juniPPPoEIfStatsRxInvTags=_JuniPPPoEIfStatsRxInvTags_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,9),_JuniPPPoEIfStatsRxInvTags_Type())
juniPPPoEIfStatsRxInvTags.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvTags.setStatus(_B)
_JuniPPPoEIfStatsRxInvSession_Type=Counter32
_JuniPPPoEIfStatsRxInvSession_Object=MibTableColumn
juniPPPoEIfStatsRxInvSession=_JuniPPPoEIfStatsRxInvSession_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,10),_JuniPPPoEIfStatsRxInvSession_Type())
juniPPPoEIfStatsRxInvSession.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvSession.setStatus(_E)
_JuniPPPoEIfStatsRxInvTypes_Type=Counter32
_JuniPPPoEIfStatsRxInvTypes_Object=MibTableColumn
juniPPPoEIfStatsRxInvTypes=_JuniPPPoEIfStatsRxInvTypes_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,11),_JuniPPPoEIfStatsRxInvTypes_Type())
juniPPPoEIfStatsRxInvTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvTypes.setStatus(_B)
_JuniPPPoEIfStatsRxInvPackets_Type=Counter32
_JuniPPPoEIfStatsRxInvPackets_Object=MibTableColumn
juniPPPoEIfStatsRxInvPackets=_JuniPPPoEIfStatsRxInvPackets_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,12),_JuniPPPoEIfStatsRxInvPackets_Type())
juniPPPoEIfStatsRxInvPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvPackets.setStatus(_B)
_JuniPPPoEIfStatsRxInsufficientResources_Type=Counter32
_JuniPPPoEIfStatsRxInsufficientResources_Object=MibTableColumn
juniPPPoEIfStatsRxInsufficientResources=_JuniPPPoEIfStatsRxInsufficientResources_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,13),_JuniPPPoEIfStatsRxInsufficientResources_Type())
juniPPPoEIfStatsRxInsufficientResources.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInsufficientResources.setStatus(_B)
_JuniPPPoEIfStatsTxPADM_Type=Counter32
_JuniPPPoEIfStatsTxPADM_Object=MibTableColumn
juniPPPoEIfStatsTxPADM=_JuniPPPoEIfStatsTxPADM_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,14),_JuniPPPoEIfStatsTxPADM_Type())
juniPPPoEIfStatsTxPADM.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsTxPADM.setStatus(_B)
_JuniPPPoEIfStatsTxPADN_Type=Counter32
_JuniPPPoEIfStatsTxPADN_Object=MibTableColumn
juniPPPoEIfStatsTxPADN=_JuniPPPoEIfStatsTxPADN_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,15),_JuniPPPoEIfStatsTxPADN_Type())
juniPPPoEIfStatsTxPADN.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsTxPADN.setStatus(_B)
_JuniPPPoEIfStatsRxInvTagLength_Type=Counter32
_JuniPPPoEIfStatsRxInvTagLength_Object=MibTableColumn
juniPPPoEIfStatsRxInvTagLength=_JuniPPPoEIfStatsRxInvTagLength_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,16),_JuniPPPoEIfStatsRxInvTagLength_Type())
juniPPPoEIfStatsRxInvTagLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvTagLength.setStatus(_B)
_JuniPPPoEIfStatsRxInvLength_Type=Counter32
_JuniPPPoEIfStatsRxInvLength_Object=MibTableColumn
juniPPPoEIfStatsRxInvLength=_JuniPPPoEIfStatsRxInvLength_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,17),_JuniPPPoEIfStatsRxInvLength_Type())
juniPPPoEIfStatsRxInvLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvLength.setStatus(_B)
_JuniPPPoEIfStatsRxInvPadISession_Type=Counter32
_JuniPPPoEIfStatsRxInvPadISession_Object=MibTableColumn
juniPPPoEIfStatsRxInvPadISession=_JuniPPPoEIfStatsRxInvPadISession_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,18),_JuniPPPoEIfStatsRxInvPadISession_Type())
juniPPPoEIfStatsRxInvPadISession.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvPadISession.setStatus(_B)
_JuniPPPoEIfStatsRxInvPadRSession_Type=Counter32
_JuniPPPoEIfStatsRxInvPadRSession_Object=MibTableColumn
juniPPPoEIfStatsRxInvPadRSession=_JuniPPPoEIfStatsRxInvPadRSession_Object((1,3,6,1,4,1,4874,2,2,18,1,1,3,1,19),_JuniPPPoEIfStatsRxInvPadRSession_Type())
juniPPPoEIfStatsRxInvPadRSession.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfStatsRxInvPadRSession.setStatus(_B)
_JuniPPPoEIfLockoutTable_Object=MibTable
juniPPPoEIfLockoutTable=_JuniPPPoEIfLockoutTable_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4))
if mibBuilder.loadTexts:juniPPPoEIfLockoutTable.setStatus(_B)
_JuniPPPoEIfLockoutEntry_Object=MibTableRow
juniPPPoEIfLockoutEntry=_JuniPPPoEIfLockoutEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4,1))
juniPPPoEIfLockoutEntry.setIndexNames((0,_A,_F),(0,_A,_AC))
if mibBuilder.loadTexts:juniPPPoEIfLockoutEntry.setStatus(_B)
_JuniPPPoEIfLockoutClientAddress_Type=MacAddress
_JuniPPPoEIfLockoutClientAddress_Object=MibTableColumn
juniPPPoEIfLockoutClientAddress=_JuniPPPoEIfLockoutClientAddress_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4,1,1),_JuniPPPoEIfLockoutClientAddress_Type())
juniPPPoEIfLockoutClientAddress.setMaxAccess(_r)
if mibBuilder.loadTexts:juniPPPoEIfLockoutClientAddress.setStatus(_B)
class _JuniPPPoEIfLockoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniPPPoEIfLockoutTime_Type.__name__=_I
_JuniPPPoEIfLockoutTime_Object=MibTableColumn
juniPPPoEIfLockoutTime=_JuniPPPoEIfLockoutTime_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4,1,2),_JuniPPPoEIfLockoutTime_Type())
juniPPPoEIfLockoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfLockoutTime.setStatus(_B)
class _JuniPPPoEIfLockoutElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniPPPoEIfLockoutElapsedTime_Type.__name__=_I
_JuniPPPoEIfLockoutElapsedTime_Object=MibTableColumn
juniPPPoEIfLockoutElapsedTime=_JuniPPPoEIfLockoutElapsedTime_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4,1,3),_JuniPPPoEIfLockoutElapsedTime_Type())
juniPPPoEIfLockoutElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfLockoutElapsedTime.setStatus(_B)
class _JuniPPPoEIfLockoutNextTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniPPPoEIfLockoutNextTime_Type.__name__=_I
_JuniPPPoEIfLockoutNextTime_Object=MibTableColumn
juniPPPoEIfLockoutNextTime=_JuniPPPoEIfLockoutNextTime_Object((1,3,6,1,4,1,4874,2,2,18,1,1,4,1,4),_JuniPPPoEIfLockoutNextTime_Type())
juniPPPoEIfLockoutNextTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEIfLockoutNextTime.setStatus(_B)
_JuniPPPoESubIfLayer_ObjectIdentity=ObjectIdentity
juniPPPoESubIfLayer=_JuniPPPoESubIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,2))
_JuniPPPoESubIfNextIfIndex_Type=JuniNextIfIndex
_JuniPPPoESubIfNextIfIndex_Object=MibScalar
juniPPPoESubIfNextIfIndex=_JuniPPPoESubIfNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,2,1),_JuniPPPoESubIfNextIfIndex_Type())
juniPPPoESubIfNextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESubIfNextIfIndex.setStatus(_B)
_JuniPPPoESubIfTable_Object=MibTable
juniPPPoESubIfTable=_JuniPPPoESubIfTable_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2))
if mibBuilder.loadTexts:juniPPPoESubIfTable.setStatus(_B)
_JuniPPPoESubIfEntry_Object=MibTableRow
juniPPPoESubIfEntry=_JuniPPPoESubIfEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1))
juniPPPoESubIfEntry.setIndexNames((0,_A,_AD))
if mibBuilder.loadTexts:juniPPPoESubIfEntry.setStatus(_B)
_JuniPPPoESubIfIndex_Type=InterfaceIndex
_JuniPPPoESubIfIndex_Object=MibTableColumn
juniPPPoESubIfIndex=_JuniPPPoESubIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,1),_JuniPPPoESubIfIndex_Type())
juniPPPoESubIfIndex.setMaxAccess(_r)
if mibBuilder.loadTexts:juniPPPoESubIfIndex.setStatus(_B)
_JuniPPPoESubIfRowStatus_Type=RowStatus
_JuniPPPoESubIfRowStatus_Object=MibTableColumn
juniPPPoESubIfRowStatus=_JuniPPPoESubIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,2),_JuniPPPoESubIfRowStatus_Type())
juniPPPoESubIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoESubIfRowStatus.setStatus(_B)
_JuniPPPoESubIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniPPPoESubIfLowerIfIndex_Object=MibTableColumn
juniPPPoESubIfLowerIfIndex=_JuniPPPoESubIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,3),_JuniPPPoESubIfLowerIfIndex_Type())
juniPPPoESubIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoESubIfLowerIfIndex.setStatus(_B)
class _JuniPPPoESubIfId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniPPPoESubIfId_Type.__name__=_I
_JuniPPPoESubIfId_Object=MibTableColumn
juniPPPoESubIfId=_JuniPPPoESubIfId_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,4),_JuniPPPoESubIfId_Type())
juniPPPoESubIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoESubIfId.setStatus(_B)
class _JuniPPPoESubIfSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniPPPoESubIfSessionId_Type.__name__=_I
_JuniPPPoESubIfSessionId_Object=MibTableColumn
juniPPPoESubIfSessionId=_JuniPPPoESubIfSessionId_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,5),_JuniPPPoESubIfSessionId_Type())
juniPPPoESubIfSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESubIfSessionId.setStatus(_B)
class _JuniPPPoESubIfMotm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPPPoESubIfMotm_Type.__name__=_b
_JuniPPPoESubIfMotm_Object=MibTableColumn
juniPPPoESubIfMotm=_JuniPPPoESubIfMotm_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,6),_JuniPPPoESubIfMotm_Type())
juniPPPoESubIfMotm.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoESubIfMotm.setStatus(_B)
class _JuniPPPoESubIfUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPPPoESubIfUrl_Type.__name__=_b
_JuniPPPoESubIfUrl_Object=MibTableColumn
juniPPPoESubIfUrl=_JuniPPPoESubIfUrl_Object((1,3,6,1,4,1,4874,2,2,18,1,2,2,1,7),_JuniPPPoESubIfUrl_Type())
juniPPPoESubIfUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoESubIfUrl.setStatus(_B)
_JuniPPPoEGlobal_ObjectIdentity=ObjectIdentity
juniPPPoEGlobal=_JuniPPPoEGlobal_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,3))
class _JuniPPPoEGlobalMotm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPPPoEGlobalMotm_Type.__name__=_b
_JuniPPPoEGlobalMotm_Object=MibScalar
juniPPPoEGlobalMotm=_JuniPPPoEGlobalMotm_Object((1,3,6,1,4,1,4874,2,2,18,1,3,1),_JuniPPPoEGlobalMotm_Type())
juniPPPoEGlobalMotm.setMaxAccess(_q)
if mibBuilder.loadTexts:juniPPPoEGlobalMotm.setStatus(_B)
_JuniPPPoEProfile_ObjectIdentity=ObjectIdentity
juniPPPoEProfile=_JuniPPPoEProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,4))
_JuniPPPoEProfileTable_Object=MibTable
juniPPPoEProfileTable=_JuniPPPoEProfileTable_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1))
if mibBuilder.loadTexts:juniPPPoEProfileTable.setStatus(_g)
_JuniPPPoEProfileEntry_Object=MibTableRow
juniPPPoEProfileEntry=_JuniPPPoEProfileEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1,1))
juniPPPoEProfileEntry.setIndexNames((0,_A,_AE))
if mibBuilder.loadTexts:juniPPPoEProfileEntry.setStatus(_g)
_JuniPPPoEProfileIndex_Type=Unsigned32
_JuniPPPoEProfileIndex_Object=MibTableColumn
juniPPPoEProfileIndex=_JuniPPPoEProfileIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1,1,1),_JuniPPPoEProfileIndex_Type())
juniPPPoEProfileIndex.setMaxAccess(_r)
if mibBuilder.loadTexts:juniPPPoEProfileIndex.setStatus(_g)
_JuniPPPoEProfileRowStatus_Type=RowStatus
_JuniPPPoEProfileRowStatus_Object=MibTableColumn
juniPPPoEProfileRowStatus=_JuniPPPoEProfileRowStatus_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1,1,2),_JuniPPPoEProfileRowStatus_Type())
juniPPPoEProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEProfileRowStatus.setStatus(_g)
class _JuniPPPoEProfileMotm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPPPoEProfileMotm_Type.__name__=_b
_JuniPPPoEProfileMotm_Object=MibTableColumn
juniPPPoEProfileMotm=_JuniPPPoEProfileMotm_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1,1,3),_JuniPPPoEProfileMotm_Type())
juniPPPoEProfileMotm.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEProfileMotm.setStatus(_g)
class _JuniPPPoEProfileUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPPPoEProfileUrl_Type.__name__=_b
_JuniPPPoEProfileUrl_Object=MibTableColumn
juniPPPoEProfileUrl=_JuniPPPoEProfileUrl_Object((1,3,6,1,4,1,4874,2,2,18,1,4,1,1,4),_JuniPPPoEProfileUrl_Type())
juniPPPoEProfileUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEProfileUrl.setStatus(_g)
_JuniPPPoESummary_ObjectIdentity=ObjectIdentity
juniPPPoESummary=_JuniPPPoESummary_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,5))
_JuniPPPoEMajorInterfaceCount_Type=Integer32
_JuniPPPoEMajorInterfaceCount_Object=MibScalar
juniPPPoEMajorInterfaceCount=_JuniPPPoEMajorInterfaceCount_Object((1,3,6,1,4,1,4874,2,2,18,1,5,1),_JuniPPPoEMajorInterfaceCount_Type())
juniPPPoEMajorInterfaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEMajorInterfaceCount.setStatus(_B)
_JuniPPPoESummaryMajorIfAdminUp_Type=Integer32
_JuniPPPoESummaryMajorIfAdminUp_Object=MibScalar
juniPPPoESummaryMajorIfAdminUp=_JuniPPPoESummaryMajorIfAdminUp_Object((1,3,6,1,4,1,4874,2,2,18,1,5,2),_JuniPPPoESummaryMajorIfAdminUp_Type())
juniPPPoESummaryMajorIfAdminUp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfAdminUp.setStatus(_B)
_JuniPPPoESummaryMajorIfAdminDown_Type=Integer32
_JuniPPPoESummaryMajorIfAdminDown_Object=MibScalar
juniPPPoESummaryMajorIfAdminDown=_JuniPPPoESummaryMajorIfAdminDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,3),_JuniPPPoESummaryMajorIfAdminDown_Type())
juniPPPoESummaryMajorIfAdminDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfAdminDown.setStatus(_B)
_JuniPPPoESummaryMajorIfOperUp_Type=Integer32
_JuniPPPoESummaryMajorIfOperUp_Object=MibScalar
juniPPPoESummaryMajorIfOperUp=_JuniPPPoESummaryMajorIfOperUp_Object((1,3,6,1,4,1,4874,2,2,18,1,5,4),_JuniPPPoESummaryMajorIfOperUp_Type())
juniPPPoESummaryMajorIfOperUp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfOperUp.setStatus(_B)
_JuniPPPoESummaryMajorIfOperDown_Type=Integer32
_JuniPPPoESummaryMajorIfOperDown_Object=MibScalar
juniPPPoESummaryMajorIfOperDown=_JuniPPPoESummaryMajorIfOperDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,5),_JuniPPPoESummaryMajorIfOperDown_Type())
juniPPPoESummaryMajorIfOperDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfOperDown.setStatus(_B)
_JuniPPPoESummaryMajorIfLowerLayerDown_Type=Integer32
_JuniPPPoESummaryMajorIfLowerLayerDown_Object=MibScalar
juniPPPoESummaryMajorIfLowerLayerDown=_JuniPPPoESummaryMajorIfLowerLayerDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,6),_JuniPPPoESummaryMajorIfLowerLayerDown_Type())
juniPPPoESummaryMajorIfLowerLayerDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfLowerLayerDown.setStatus(_B)
_JuniPPPoESummaryMajorIfNotPresent_Type=Integer32
_JuniPPPoESummaryMajorIfNotPresent_Object=MibScalar
juniPPPoESummaryMajorIfNotPresent=_JuniPPPoESummaryMajorIfNotPresent_Object((1,3,6,1,4,1,4874,2,2,18,1,5,7),_JuniPPPoESummaryMajorIfNotPresent_Type())
juniPPPoESummaryMajorIfNotPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummaryMajorIfNotPresent.setStatus(_B)
_JuniPPPoESummarySubInterfaceCount_Type=Integer32
_JuniPPPoESummarySubInterfaceCount_Object=MibScalar
juniPPPoESummarySubInterfaceCount=_JuniPPPoESummarySubInterfaceCount_Object((1,3,6,1,4,1,4874,2,2,18,1,5,8),_JuniPPPoESummarySubInterfaceCount_Type())
juniPPPoESummarySubInterfaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubInterfaceCount.setStatus(_B)
_JuniPPPoESummarySubIfAdminUp_Type=Integer32
_JuniPPPoESummarySubIfAdminUp_Object=MibScalar
juniPPPoESummarySubIfAdminUp=_JuniPPPoESummarySubIfAdminUp_Object((1,3,6,1,4,1,4874,2,2,18,1,5,9),_JuniPPPoESummarySubIfAdminUp_Type())
juniPPPoESummarySubIfAdminUp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfAdminUp.setStatus(_B)
_JuniPPPoESummarySubIfAdminDown_Type=Integer32
_JuniPPPoESummarySubIfAdminDown_Object=MibScalar
juniPPPoESummarySubIfAdminDown=_JuniPPPoESummarySubIfAdminDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,10),_JuniPPPoESummarySubIfAdminDown_Type())
juniPPPoESummarySubIfAdminDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfAdminDown.setStatus(_B)
_JuniPPPoESummarySubIfOperUp_Type=Integer32
_JuniPPPoESummarySubIfOperUp_Object=MibScalar
juniPPPoESummarySubIfOperUp=_JuniPPPoESummarySubIfOperUp_Object((1,3,6,1,4,1,4874,2,2,18,1,5,11),_JuniPPPoESummarySubIfOperUp_Type())
juniPPPoESummarySubIfOperUp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfOperUp.setStatus(_B)
_JuniPPPoESummarySubIfOperDown_Type=Integer32
_JuniPPPoESummarySubIfOperDown_Object=MibScalar
juniPPPoESummarySubIfOperDown=_JuniPPPoESummarySubIfOperDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,12),_JuniPPPoESummarySubIfOperDown_Type())
juniPPPoESummarySubIfOperDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfOperDown.setStatus(_B)
_JuniPPPoESummarySubIfLowerLayerDown_Type=Integer32
_JuniPPPoESummarySubIfLowerLayerDown_Object=MibScalar
juniPPPoESummarySubIfLowerLayerDown=_JuniPPPoESummarySubIfLowerLayerDown_Object((1,3,6,1,4,1,4874,2,2,18,1,5,13),_JuniPPPoESummarySubIfLowerLayerDown_Type())
juniPPPoESummarySubIfLowerLayerDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfLowerLayerDown.setStatus(_B)
_JuniPPPoESummarySubIfNotPresent_Type=Integer32
_JuniPPPoESummarySubIfNotPresent_Object=MibScalar
juniPPPoESummarySubIfNotPresent=_JuniPPPoESummarySubIfNotPresent_Object((1,3,6,1,4,1,4874,2,2,18,1,5,14),_JuniPPPoESummarySubIfNotPresent_Type())
juniPPPoESummarySubIfNotPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoESummarySubIfNotPresent.setStatus(_B)
_JuniPPPoEServices_ObjectIdentity=ObjectIdentity
juniPPPoEServices=_JuniPPPoEServices_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,1,6))
_JuniPPPoEServiceNameTableNextIndex_Type=Unsigned32
_JuniPPPoEServiceNameTableNextIndex_Object=MibScalar
juniPPPoEServiceNameTableNextIndex=_JuniPPPoEServiceNameTableNextIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,6,1),_JuniPPPoEServiceNameTableNextIndex_Type())
juniPPPoEServiceNameTableNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableNextIndex.setStatus(_B)
_JuniPPPoEServiceNameTableTable_Object=MibTable
juniPPPoEServiceNameTableTable=_JuniPPPoEServiceNameTableTable_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2))
if mibBuilder.loadTexts:juniPPPoEServiceNameTableTable.setStatus(_B)
_JuniPPPoEServiceNameTableEntry_Object=MibTableRow
juniPPPoEServiceNameTableEntry=_JuniPPPoEServiceNameTableEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1))
juniPPPoEServiceNameTableEntry.setIndexNames((0,_A,_w))
if mibBuilder.loadTexts:juniPPPoEServiceNameTableEntry.setStatus(_B)
_JuniPPPoEServiceNameTableIndex_Type=Unsigned32
_JuniPPPoEServiceNameTableIndex_Object=MibTableColumn
juniPPPoEServiceNameTableIndex=_JuniPPPoEServiceNameTableIndex_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1,1),_JuniPPPoEServiceNameTableIndex_Type())
juniPPPoEServiceNameTableIndex.setMaxAccess(_r)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableIndex.setStatus(_B)
class _JuniPPPoEServiceNameTableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniPPPoEServiceNameTableName_Type.__name__=_b
_JuniPPPoEServiceNameTableName_Object=MibTableColumn
juniPPPoEServiceNameTableName=_JuniPPPoEServiceNameTableName_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1,2),_JuniPPPoEServiceNameTableName_Type())
juniPPPoEServiceNameTableName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableName.setStatus(_B)
_JuniPPPoEServiceNameTableEmptyAction_Type=JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameTableEmptyAction_Object=MibTableColumn
juniPPPoEServiceNameTableEmptyAction=_JuniPPPoEServiceNameTableEmptyAction_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1,3),_JuniPPPoEServiceNameTableEmptyAction_Type())
juniPPPoEServiceNameTableEmptyAction.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableEmptyAction.setStatus(_B)
_JuniPPPoEServiceNameTableRowStatus_Type=RowStatus
_JuniPPPoEServiceNameTableRowStatus_Object=MibTableColumn
juniPPPoEServiceNameTableRowStatus=_JuniPPPoEServiceNameTableRowStatus_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1,4),_JuniPPPoEServiceNameTableRowStatus_Type())
juniPPPoEServiceNameTableRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableRowStatus.setStatus(_B)
_JuniPPPoEServiceNameTableUnknownAction_Type=JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameTableUnknownAction_Object=MibTableColumn
juniPPPoEServiceNameTableUnknownAction=_JuniPPPoEServiceNameTableUnknownAction_Object((1,3,6,1,4,1,4874,2,2,18,1,6,2,1,5),_JuniPPPoEServiceNameTableUnknownAction_Type())
juniPPPoEServiceNameTableUnknownAction.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameTableUnknownAction.setStatus(_B)
_JuniPPPoEServiceNameTable_Object=MibTable
juniPPPoEServiceNameTable=_JuniPPPoEServiceNameTable_Object((1,3,6,1,4,1,4874,2,2,18,1,6,3))
if mibBuilder.loadTexts:juniPPPoEServiceNameTable.setStatus(_B)
_JuniPPPoEServiceNameEntry_Object=MibTableRow
juniPPPoEServiceNameEntry=_JuniPPPoEServiceNameEntry_Object((1,3,6,1,4,1,4874,2,2,18,1,6,3,1))
juniPPPoEServiceNameEntry.setIndexNames((0,_A,_w),(0,_A,_AF))
if mibBuilder.loadTexts:juniPPPoEServiceNameEntry.setStatus(_B)
class _JuniPPPoEServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniPPPoEServiceName_Type.__name__=_b
_JuniPPPoEServiceName_Object=MibTableColumn
juniPPPoEServiceName=_JuniPPPoEServiceName_Object((1,3,6,1,4,1,4874,2,2,18,1,6,3,1,1),_JuniPPPoEServiceName_Type())
juniPPPoEServiceName.setMaxAccess(_r)
if mibBuilder.loadTexts:juniPPPoEServiceName.setStatus(_B)
_JuniPPPoEServiceNameAction_Type=JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameAction_Object=MibTableColumn
juniPPPoEServiceNameAction=_JuniPPPoEServiceNameAction_Object((1,3,6,1,4,1,4874,2,2,18,1,6,3,1,2),_JuniPPPoEServiceNameAction_Type())
juniPPPoEServiceNameAction.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameAction.setStatus(_B)
_JuniPPPoEServiceNameRowStatus_Type=RowStatus
_JuniPPPoEServiceNameRowStatus_Object=MibTableColumn
juniPPPoEServiceNameRowStatus=_JuniPPPoEServiceNameRowStatus_Object((1,3,6,1,4,1,4874,2,2,18,1,6,3,1,3),_JuniPPPoEServiceNameRowStatus_Type())
juniPPPoEServiceNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniPPPoEServiceNameRowStatus.setStatus(_B)
_JuniPPPoEConformance_ObjectIdentity=ObjectIdentity
juniPPPoEConformance=_JuniPPPoEConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,4))
_JuniPPPoEGroups_ObjectIdentity=ObjectIdentity
juniPPPoEGroups=_JuniPPPoEGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,4,4))
_JuniPPPoECompliances_ObjectIdentity=ObjectIdentity
juniPPPoECompliances=_JuniPPPoECompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,18,4,5))
juniPPPoEGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,1))
juniPPPoEGroup.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:juniPPPoEGroup.setStatus(_E)
juniPPPoESubIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,2))
juniPPPoESubIfGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:juniPPPoESubIfGroup.setStatus(_E)
juniPPPoEProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,3))
juniPPPoEProfileGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:juniPPPoEProfileGroup.setStatus(_g)
juniPPPoEGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,4))
juniPPPoEGroup2.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup2.setStatus(_E)
juniPPPoESubIfGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,5))
juniPPPoESubIfGroup2.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:juniPPPoESubIfGroup2.setStatus(_B)
juniPPPoESummaryGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,6))
juniPPPoESummaryGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:juniPPPoESummaryGroup.setStatus(_B)
juniPPPoEGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,7))
juniPPPoEGroup3.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup3.setStatus(_E)
juniPPPoEGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,8))
juniPPPoEGroup4.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup4.setStatus(_E)
juniPPPoEGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,9))
juniPPPoEGroup5.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup5.setStatus(_E)
juniPPPoEGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,10))
juniPPPoEGroup6.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_j),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_k),(_A,_l),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_m),(_A,_n),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup6.setStatus(_E)
juniPPPoEServiceNameTableGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,11))
juniPPPoEServiceNameTableGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:juniPPPoEServiceNameTableGroup.setStatus(_E)
juniPPPoEGroup7=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,12))
juniPPPoEGroup7.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_j),(_A,_s),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_k),(_A,_l),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_m),(_A,_n),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup7.setStatus(_E)
juniPPPoEGroup8=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,13))
juniPPPoEGroup8.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_j),(_A,_s),(_A,_t),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_k),(_A,_l),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_m),(_A,_n),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup8.setStatus(_B)
juniPPPoELockoutTableGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,14))
juniPPPoELockoutTableGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:juniPPPoELockoutTableGroup.setStatus(_B)
juniPPPoEGroup9=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,15))
juniPPPoEGroup9.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_j),(_A,_s),(_A,_t),(_A,_A8),(_A,_A9),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_k),(_A,_l),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_m),(_A,_n),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup9.setStatus(_E)
juniPPPoEGroup10=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,16))
juniPPPoEGroup10.setObjects(*((_A,_J),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_j),(_A,_s),(_A,_t),(_A,_A8),(_A,_A9),(_A,_Ac),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_k),(_A,_l),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_m),(_A,_n),(_A,_a)))
if mibBuilder.loadTexts:juniPPPoEGroup10.setStatus(_B)
juniPPPoEServiceNameTableGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,18,4,4,17))
juniPPPoEServiceNameTableGroup1.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_Ad)))
if mibBuilder.loadTexts:juniPPPoEServiceNameTableGroup1.setStatus(_B)
juniPPPoECompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,1))
juniPPPoECompliance.setObjects(*((_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:juniPPPoECompliance.setStatus(_E)
juniPPPoECompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,2))
juniPPPoECompliance2.setObjects(*((_A,_u),(_A,_G),(_A,_AA)))
if mibBuilder.loadTexts:juniPPPoECompliance2.setStatus(_E)
juniPPPoECompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,3))
juniPPPoECompliance3.setObjects(*((_A,_u),(_A,_G),(_A,_AA),(_A,_H)))
if mibBuilder.loadTexts:juniPPPoECompliance3.setStatus(_E)
juniPPPoECompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,4))
juniPPPoECompliance4.setObjects(*((_A,_u),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:juniPPPoECompliance4.setStatus(_E)
juniPPPoECompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,5))
juniPPPoECompliance5.setObjects(*((_A,_Ag),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:juniPPPoECompliance5.setStatus(_E)
juniPPPoECompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,6))
juniPPPoECompliance6.setObjects(*((_A,_Ah),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:juniPPPoECompliance6.setStatus(_E)
juniPPPoECompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,7))
juniPPPoECompliance7.setObjects(*((_A,_Ai),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:juniPPPoECompliance7.setStatus(_E)
juniPPPoECompliance8=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,8))
juniPPPoECompliance8.setObjects(*((_A,_Aj),(_A,_G),(_A,_H),(_A,_o)))
if mibBuilder.loadTexts:juniPPPoECompliance8.setStatus(_E)
juniPPPoECompliance9=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,9))
juniPPPoECompliance9.setObjects(*((_A,_Ak),(_A,_G),(_A,_H),(_A,_o)))
if mibBuilder.loadTexts:juniPPPoECompliance9.setStatus(_E)
juniPPPoECompliance10=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,10))
juniPPPoECompliance10.setObjects(*((_A,_Al),(_A,_G),(_A,_H),(_A,_o)))
if mibBuilder.loadTexts:juniPPPoECompliance10.setStatus(_E)
juniPPPoECompliance11=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,11))
juniPPPoECompliance11.setObjects(*((_A,_Am),(_A,_G),(_A,_H),(_A,_o),(_A,_v)))
if mibBuilder.loadTexts:juniPPPoECompliance11.setStatus(_E)
juniPPPoECompliance12=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,12))
juniPPPoECompliance12.setObjects(*((_A,_AB),(_A,_G),(_A,_H),(_A,_o),(_A,_v)))
if mibBuilder.loadTexts:juniPPPoECompliance12.setStatus(_E)
juniPPPoECompliance13=ModuleCompliance((1,3,6,1,4,1,4874,2,2,18,4,5,13))
juniPPPoECompliance13.setObjects(*((_A,_AB),(_A,_G),(_A,_H),(_A,_An),(_A,_v)))
if mibBuilder.loadTexts:juniPPPoECompliance13.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniPPPoEServiceNameAction':JuniPPPoEServiceNameAction,'juniPPPoEMIB':juniPPPoEMIB,'juniPPPoEObjects':juniPPPoEObjects,'juniPPPoEIfLayer':juniPPPoEIfLayer,_J:juniPPPoENextIfIndex,'juniPPPoEIfTable':juniPPPoEIfTable,'juniPPPoEIfEntry':juniPPPoEIfEntry,_F:juniPPPoEIfIfIndex,_K:juniPPPoEIfMaxNumSessions,_L:juniPPPoEIfRowStatus,_M:juniPPPoEIfLowerIfIndex,_c:juniPPPoEIfAcName,_d:juniPPPoEIfDupProtect,_e:juniPPPoEIfPADIFlag,_f:juniPPPoEIfAutoconfig,_j:juniPPPoEIfServiceNameTable,_s:juniPPPoEIfPadrRemoteCircuitIdCapture,_t:juniPPPoEIfMtu,_A8:juniPPPoEIfLockoutMin,_A9:juniPPPoEIfLockoutMax,_Ac:juniPPPoEMaxSessionVsa,'juniPPPoEIfStatsTable':juniPPPoEIfStatsTable,'juniPPPoEIfStatsEntry':juniPPPoEIfStatsEntry,_N:juniPPPoEIfStatsRxPADI,_O:juniPPPoEIfStatsTxPADO,_P:juniPPPoEIfStatsRxPADR,_Q:juniPPPoEIfStatsTxPADS,_R:juniPPPoEIfStatsRxPADT,_S:juniPPPoEIfStatsTxPADT,_T:juniPPPoEIfStatsRxInvVersion,_U:juniPPPoEIfStatsRxInvCode,_V:juniPPPoEIfStatsRxInvTags,_i:juniPPPoEIfStatsRxInvSession,_W:juniPPPoEIfStatsRxInvTypes,_X:juniPPPoEIfStatsRxInvPackets,_Y:juniPPPoEIfStatsRxInsufficientResources,_Z:juniPPPoEIfStatsTxPADM,_h:juniPPPoEIfStatsTxPADN,_k:juniPPPoEIfStatsRxInvTagLength,_l:juniPPPoEIfStatsRxInvLength,_m:juniPPPoEIfStatsRxInvPadISession,_n:juniPPPoEIfStatsRxInvPadRSession,'juniPPPoEIfLockoutTable':juniPPPoEIfLockoutTable,'juniPPPoEIfLockoutEntry':juniPPPoEIfLockoutEntry,_AC:juniPPPoEIfLockoutClientAddress,_AZ:juniPPPoEIfLockoutTime,_Aa:juniPPPoEIfLockoutElapsedTime,_Ab:juniPPPoEIfLockoutNextTime,'juniPPPoESubIfLayer':juniPPPoESubIfLayer,_x:juniPPPoESubIfNextIfIndex,'juniPPPoESubIfTable':juniPPPoESubIfTable,'juniPPPoESubIfEntry':juniPPPoESubIfEntry,_AD:juniPPPoESubIfIndex,_y:juniPPPoESubIfRowStatus,_z:juniPPPoESubIfLowerIfIndex,_A0:juniPPPoESubIfId,_A1:juniPPPoESubIfSessionId,_AK:juniPPPoESubIfMotm,_AJ:juniPPPoESubIfUrl,'juniPPPoEGlobal':juniPPPoEGlobal,_a:juniPPPoEGlobalMotm,'juniPPPoEProfile':juniPPPoEProfile,'juniPPPoEProfileTable':juniPPPoEProfileTable,'juniPPPoEProfileEntry':juniPPPoEProfileEntry,_AE:juniPPPoEProfileIndex,_AG:juniPPPoEProfileRowStatus,_AI:juniPPPoEProfileMotm,_AH:juniPPPoEProfileUrl,'juniPPPoESummary':juniPPPoESummary,_AL:juniPPPoEMajorInterfaceCount,_AM:juniPPPoESummaryMajorIfAdminUp,_AN:juniPPPoESummaryMajorIfAdminDown,_AO:juniPPPoESummaryMajorIfOperUp,_AP:juniPPPoESummaryMajorIfOperDown,_AR:juniPPPoESummaryMajorIfLowerLayerDown,_AQ:juniPPPoESummaryMajorIfNotPresent,_AS:juniPPPoESummarySubInterfaceCount,_AT:juniPPPoESummarySubIfAdminUp,_AU:juniPPPoESummarySubIfAdminDown,_AV:juniPPPoESummarySubIfOperUp,_AW:juniPPPoESummarySubIfOperDown,_AY:juniPPPoESummarySubIfLowerLayerDown,_AX:juniPPPoESummarySubIfNotPresent,'juniPPPoEServices':juniPPPoEServices,_A2:juniPPPoEServiceNameTableNextIndex,'juniPPPoEServiceNameTableTable':juniPPPoEServiceNameTableTable,'juniPPPoEServiceNameTableEntry':juniPPPoEServiceNameTableEntry,_w:juniPPPoEServiceNameTableIndex,_A3:juniPPPoEServiceNameTableName,_A4:juniPPPoEServiceNameTableEmptyAction,_A5:juniPPPoEServiceNameTableRowStatus,_Ad:juniPPPoEServiceNameTableUnknownAction,'juniPPPoEServiceNameTable':juniPPPoEServiceNameTable,'juniPPPoEServiceNameEntry':juniPPPoEServiceNameEntry,_AF:juniPPPoEServiceName,_A6:juniPPPoEServiceNameAction,_A7:juniPPPoEServiceNameRowStatus,'juniPPPoEConformance':juniPPPoEConformance,'juniPPPoEGroups':juniPPPoEGroups,_Ae:juniPPPoEGroup,_Af:juniPPPoESubIfGroup,_AA:juniPPPoEProfileGroup,_u:juniPPPoEGroup2,_G:juniPPPoESubIfGroup2,_H:juniPPPoESummaryGroup,_Ag:juniPPPoEGroup3,_Ah:juniPPPoEGroup4,_Ai:juniPPPoEGroup5,_Aj:juniPPPoEGroup6,_o:juniPPPoEServiceNameTableGroup,_Ak:juniPPPoEGroup7,_Al:juniPPPoEGroup8,_v:juniPPPoELockoutTableGroup,_Am:juniPPPoEGroup9,_AB:juniPPPoEGroup10,_An:juniPPPoEServiceNameTableGroup1,'juniPPPoECompliances':juniPPPoECompliances,'juniPPPoECompliance':juniPPPoECompliance,'juniPPPoECompliance2':juniPPPoECompliance2,'juniPPPoECompliance3':juniPPPoECompliance3,'juniPPPoECompliance4':juniPPPoECompliance4,'juniPPPoECompliance5':juniPPPoECompliance5,'juniPPPoECompliance6':juniPPPoECompliance6,'juniPPPoECompliance7':juniPPPoECompliance7,'juniPPPoECompliance8':juniPPPoECompliance8,'juniPPPoECompliance9':juniPPPoECompliance9,'juniPPPoECompliance10':juniPPPoECompliance10,'juniPPPoECompliance11':juniPPPoECompliance11,'juniPPPoECompliance12':juniPPPoECompliance12,'juniPPPoECompliance13':juniPPPoECompliance13})