_x='nwAppnEventNumber'
_w='highlow'
_v='highmed'
_u='highest'
_t='nwAppnEventFltrIfNum'
_s='nwAppnEventFltrProtocol'
_r='nwAppnFwdLsCtrLsName'
_q='nwAppnFwdLsName'
_p='nwAppnFwdIfCtrIfIndex'
_o='nwAppnIfCnTgFqName'
_n='nwAppnIfCnPtName'
_m='nwAppnIfCnPtFqName'
_l='orderly'
_k='nwAppnExtIfIndex'
_j='nwAppnFwdIfIndex'
_i='nwAppnSysLuName'
_h='nwAppnSysCpName'
_g='networknode'
_f='maximum'
_e='long'
_d='packetswitched'
_c='terrestrial'
_b='negligible'
_a='minimum'
_Z='guardedRadiation'
_Y='encrypted'
_X='guardedConduit'
_W='secureConduit'
_V='undergroundCable'
_U='publicSwitchNw'
_T='nonsecure'
_S='enable'
_R='immediate'
_Q='reset'
_P='pendingEnable'
_O='pendingDisable'
_N='delete'
_M='disable'
_L='OctetString'
_K='yes'
_J='disabled'
_I='no'
_H='enabled'
_G='CTRON-APPN-MIB'
_F='DisplayString'
_E='other'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwRtrProtoSuites,=mibBuilder.importSymbols('ROUTER-OIDS','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_NwAppnRouter_ObjectIdentity=ObjectIdentity
nwAppnRouter=_NwAppnRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5))
_NwAppnMibs_ObjectIdentity=ObjectIdentity
nwAppnMibs=_NwAppnMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,1))
_NwAppnMibRevText_Type=DisplayString
_NwAppnMibRevText_Object=MibScalar
nwAppnMibRevText=_NwAppnMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,1,1),_NwAppnMibRevText_Type())
nwAppnMibRevText.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnMibRevText.setStatus(_A)
_NwAppnComponents_ObjectIdentity=ObjectIdentity
nwAppnComponents=_NwAppnComponents_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2))
_NwAppnSystem_ObjectIdentity=ObjectIdentity
nwAppnSystem=_NwAppnSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1))
_NwAppnSysConfig_ObjectIdentity=ObjectIdentity
nwAppnSysConfig=_NwAppnSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1))
class _NwAppnSysRouterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_NwAppnSysRouterId_Type.__name__=_F
_NwAppnSysRouterId_Object=MibScalar
nwAppnSysRouterId=_NwAppnSysRouterId_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,1),_NwAppnSysRouterId_Type())
nwAppnSysRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysRouterId.setStatus(_A)
_NwAppnSysCfgLocalNode_ObjectIdentity=ObjectIdentity
nwAppnSysCfgLocalNode=_NwAppnSysCfgLocalNode_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2))
class _NwAppnSysNodeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_g,1))
_NwAppnSysNodeType_Type.__name__=_C
_NwAppnSysNodeType_Object=MibScalar
nwAppnSysNodeType=_NwAppnSysNodeType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,1),_NwAppnSysNodeType_Type())
nwAppnSysNodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnSysNodeType.setStatus(_A)
class _NwAppnSysCpAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnSysCpAlias_Type.__name__=_F
_NwAppnSysCpAlias_Object=MibScalar
nwAppnSysCpAlias=_NwAppnSysCpAlias_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,2),_NwAppnSysCpAlias_Type())
nwAppnSysCpAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysCpAlias.setStatus(_A)
class _NwAppnSysModeCosMap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnSysModeCosMap_Type.__name__=_C
_NwAppnSysModeCosMap_Object=MibScalar
nwAppnSysModeCosMap=_NwAppnSysModeCosMap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,3),_NwAppnSysModeCosMap_Type())
nwAppnSysModeCosMap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysModeCosMap.setStatus(_A)
class _NwAppnSysMdsSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnSysMdsSupport_Type.__name__=_C
_NwAppnSysMdsSupport_Object=MibScalar
nwAppnSysMdsSupport=_NwAppnSysMdsSupport_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,4),_NwAppnSysMdsSupport_Type())
nwAppnSysMdsSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMdsSupport.setStatus(_A)
class _NwAppnSysMaxLocates_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysMaxLocates_Type.__name__=_C
_NwAppnSysMaxLocates_Object=MibScalar
nwAppnSysMaxLocates=_NwAppnSysMaxLocates_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,6),_NwAppnSysMaxLocates_Type())
nwAppnSysMaxLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMaxLocates.setStatus(_A)
class _NwAppnSysDirCacheSize_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysDirCacheSize_Type.__name__=_C
_NwAppnSysDirCacheSize_Object=MibScalar
nwAppnSysDirCacheSize=_NwAppnSysDirCacheSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,7),_NwAppnSysDirCacheSize_Type())
nwAppnSysDirCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysDirCacheSize.setStatus(_A)
class _NwAppnSysMaxDirEntries_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnSysMaxDirEntries_Type.__name__=_C
_NwAppnSysMaxDirEntries_Object=MibScalar
nwAppnSysMaxDirEntries=_NwAppnSysMaxDirEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,8),_NwAppnSysMaxDirEntries_Type())
nwAppnSysMaxDirEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMaxDirEntries.setStatus(_A)
class _NwAppnSysLocateTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnSysLocateTimeout_Type.__name__=_C
_NwAppnSysLocateTimeout_Object=MibScalar
nwAppnSysLocateTimeout=_NwAppnSysLocateTimeout_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,9),_NwAppnSysLocateTimeout_Type())
nwAppnSysLocateTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysLocateTimeout.setStatus(_A)
class _NwAppnSysRegCds_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnSysRegCds_Type.__name__=_C
_NwAppnSysRegCds_Object=MibScalar
nwAppnSysRegCds=_NwAppnSysRegCds_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,10),_NwAppnSysRegCds_Type())
nwAppnSysRegCds.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysRegCds.setStatus(_A)
class _NwAppnSysMdsSendQSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysMdsSendQSize_Type.__name__=_C
_NwAppnSysMdsSendQSize_Object=MibScalar
nwAppnSysMdsSendQSize=_NwAppnSysMdsSendQSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,11),_NwAppnSysMdsSendQSize_Type())
nwAppnSysMdsSendQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMdsSendQSize.setStatus(_A)
class _NwAppnSysCosSize_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysCosSize_Type.__name__=_C
_NwAppnSysCosSize_Object=MibScalar
nwAppnSysCosSize=_NwAppnSysCosSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,12),_NwAppnSysCosSize_Type())
nwAppnSysCosSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysCosSize.setStatus(_A)
class _NwAppnSysTreeSize_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysTreeSize_Type.__name__=_C
_NwAppnSysTreeSize_Object=MibScalar
nwAppnSysTreeSize=_NwAppnSysTreeSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,13),_NwAppnSysTreeSize_Type())
nwAppnSysTreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysTreeSize.setStatus(_A)
class _NwAppnSysTreeUseLimit_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysTreeUseLimit_Type.__name__=_C
_NwAppnSysTreeUseLimit_Object=MibScalar
nwAppnSysTreeUseLimit=_NwAppnSysTreeUseLimit_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,14),_NwAppnSysTreeUseLimit_Type())
nwAppnSysTreeUseLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysTreeUseLimit.setStatus(_A)
class _NwAppnSysMaxTdmNodes_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnSysMaxTdmNodes_Type.__name__=_C
_NwAppnSysMaxTdmNodes_Object=MibScalar
nwAppnSysMaxTdmNodes=_NwAppnSysMaxTdmNodes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,15),_NwAppnSysMaxTdmNodes_Type())
nwAppnSysMaxTdmNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMaxTdmNodes.setStatus(_A)
class _NwAppnSysMaxTdmTGs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnSysMaxTdmTGs_Type.__name__=_C
_NwAppnSysMaxTdmTGs_Object=MibScalar
nwAppnSysMaxTdmTGs=_NwAppnSysMaxTdmTGs_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,16),_NwAppnSysMaxTdmTGs_Type())
nwAppnSysMaxTdmTGs.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMaxTdmTGs.setStatus(_A)
class _NwAppnSysMaxIsrSessions_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysMaxIsrSessions_Type.__name__=_C
_NwAppnSysMaxIsrSessions_Object=MibScalar
nwAppnSysMaxIsrSessions=_NwAppnSysMaxIsrSessions_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,18),_NwAppnSysMaxIsrSessions_Type())
nwAppnSysMaxIsrSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysMaxIsrSessions.setStatus(_A)
class _NwAppnSysIsrUpperThresh_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysIsrUpperThresh_Type.__name__=_C
_NwAppnSysIsrUpperThresh_Object=MibScalar
nwAppnSysIsrUpperThresh=_NwAppnSysIsrUpperThresh_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,19),_NwAppnSysIsrUpperThresh_Type())
nwAppnSysIsrUpperThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysIsrUpperThresh.setStatus(_A)
class _NwAppnSysIsrLowerThresh_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysIsrLowerThresh_Type.__name__=_C
_NwAppnSysIsrLowerThresh_Object=MibScalar
nwAppnSysIsrLowerThresh=_NwAppnSysIsrLowerThresh_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,20),_NwAppnSysIsrLowerThresh_Type())
nwAppnSysIsrLowerThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysIsrLowerThresh.setStatus(_A)
class _NwAppnSysIsrMaxRuSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwAppnSysIsrMaxRuSize_Type.__name__=_C
_NwAppnSysIsrMaxRuSize_Object=MibScalar
nwAppnSysIsrMaxRuSize=_NwAppnSysIsrMaxRuSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,21),_NwAppnSysIsrMaxRuSize_Type())
nwAppnSysIsrMaxRuSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysIsrMaxRuSize.setStatus(_A)
class _NwAppnSysIsrRcvPaceWind_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_NwAppnSysIsrRcvPaceWind_Type.__name__=_C
_NwAppnSysIsrRcvPaceWind_Object=MibScalar
nwAppnSysIsrRcvPaceWind=_NwAppnSysIsrRcvPaceWind_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,22),_NwAppnSysIsrRcvPaceWind_Type())
nwAppnSysIsrRcvPaceWind.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysIsrRcvPaceWind.setStatus(_A)
class _NwAppnSysRtAddResist_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnSysRtAddResist_Type.__name__=_C
_NwAppnSysRtAddResist_Object=MibScalar
nwAppnSysRtAddResist=_NwAppnSysRtAddResist_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,23),_NwAppnSysRtAddResist_Type())
nwAppnSysRtAddResist.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysRtAddResist.setStatus(_A)
class _NwAppnSysStopType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('abort',1),(_R,2),('quiesce',3),('quiesceIsr',4)))
_NwAppnSysStopType_Type.__name__=_C
_NwAppnSysStopType_Object=MibScalar
nwAppnSysStopType=_NwAppnSysStopType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,24),_NwAppnSysStopType_Type())
nwAppnSysStopType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysStopType.setStatus(_A)
class _NwAppnSysBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NwAppnSysBlockNum_Type.__name__=_F
_NwAppnSysBlockNum_Object=MibScalar
nwAppnSysBlockNum=_NwAppnSysBlockNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,25),_NwAppnSysBlockNum_Type())
nwAppnSysBlockNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysBlockNum.setStatus(_A)
class _NwAppnSysIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_NwAppnSysIdNum_Type.__name__=_F
_NwAppnSysIdNum_Object=MibScalar
nwAppnSysIdNum=_NwAppnSysIdNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,2,26),_NwAppnSysIdNum_Type())
nwAppnSysIdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysIdNum.setStatus(_A)
_NwAppnSysCfgTables_ObjectIdentity=ObjectIdentity
nwAppnSysCfgTables=_NwAppnSysCfgTables_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3))
_NwAppnSysLuTable_Object=MibTable
nwAppnSysLuTable=_NwAppnSysLuTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3,1))
if mibBuilder.loadTexts:nwAppnSysLuTable.setStatus(_A)
_NwAppnSysLuEntry_Object=MibTableRow
nwAppnSysLuEntry=_NwAppnSysLuEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3,1,1))
nwAppnSysLuEntry.setIndexNames((0,_G,_h),(0,_G,_i))
if mibBuilder.loadTexts:nwAppnSysLuEntry.setStatus(_A)
class _NwAppnSysCpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_NwAppnSysCpName_Type.__name__=_F
_NwAppnSysCpName_Object=MibTableColumn
nwAppnSysCpName=_NwAppnSysCpName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3,1,1,1),_NwAppnSysCpName_Type())
nwAppnSysCpName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysCpName.setStatus(_A)
class _NwAppnSysLuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnSysLuName_Type.__name__=_F
_NwAppnSysLuName_Object=MibTableColumn
nwAppnSysLuName=_NwAppnSysLuName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3,1,1,2),_NwAppnSysLuName_Type())
nwAppnSysLuName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysLuName.setStatus(_A)
class _NwAppnSysLuControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_E,1),(_N,3)))
_NwAppnSysLuControl_Type.__name__=_C
_NwAppnSysLuControl_Object=MibTableColumn
nwAppnSysLuControl=_NwAppnSysLuControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,1,3,1,1,3),_NwAppnSysLuControl_Type())
nwAppnSysLuControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysLuControl.setStatus(_A)
_NwAppnSysAdministration_ObjectIdentity=ObjectIdentity
nwAppnSysAdministration=_NwAppnSysAdministration_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2))
class _NwAppnSysAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_H,3)))
_NwAppnSysAdminStatus_Type.__name__=_C
_NwAppnSysAdminStatus_Object=MibScalar
nwAppnSysAdminStatus=_NwAppnSysAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2,1),_NwAppnSysAdminStatus_Type())
nwAppnSysAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysAdminStatus.setStatus(_A)
class _NwAppnSysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3),(_O,4),(_P,5)))
_NwAppnSysOperStatus_Type.__name__=_C
_NwAppnSysOperStatus_Object=MibScalar
nwAppnSysOperStatus=_NwAppnSysOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2,2),_NwAppnSysOperStatus_Type())
nwAppnSysOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnSysOperStatus.setStatus(_A)
class _NwAppnSysAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_Q,2)))
_NwAppnSysAdminReset_Type.__name__=_C
_NwAppnSysAdminReset_Object=MibScalar
nwAppnSysAdminReset=_NwAppnSysAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2,3),_NwAppnSysAdminReset_Type())
nwAppnSysAdminReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnSysAdminReset.setStatus(_A)
_NwAppnSysOperationalTime_Type=TimeTicks
_NwAppnSysOperationalTime_Object=MibScalar
nwAppnSysOperationalTime=_NwAppnSysOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2,4),_NwAppnSysOperationalTime_Type())
nwAppnSysOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnSysOperationalTime.setStatus(_A)
_NwAppnSysVersion_Type=DisplayString
_NwAppnSysVersion_Object=MibScalar
nwAppnSysVersion=_NwAppnSysVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,1,2,5),_NwAppnSysVersion_Type())
nwAppnSysVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnSysVersion.setStatus(_A)
_NwAppnForwarding_ObjectIdentity=ObjectIdentity
nwAppnForwarding=_NwAppnForwarding_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2))
_NwAppnFwdSystem_ObjectIdentity=ObjectIdentity
nwAppnFwdSystem=_NwAppnFwdSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1))
_NwAppnFwdCounters_ObjectIdentity=ObjectIdentity
nwAppnFwdCounters=_NwAppnFwdCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1))
class _NwAppnFwdCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnFwdCtrAdminStatus_Type.__name__=_C
_NwAppnFwdCtrAdminStatus_Object=MibScalar
nwAppnFwdCtrAdminStatus=_NwAppnFwdCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,1),_NwAppnFwdCtrAdminStatus_Type())
nwAppnFwdCtrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdCtrAdminStatus.setStatus(_A)
class _NwAppnFwdCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_Q,2)))
_NwAppnFwdCtrReset_Type.__name__=_C
_NwAppnFwdCtrReset_Object=MibScalar
nwAppnFwdCtrReset=_NwAppnFwdCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,2),_NwAppnFwdCtrReset_Type())
nwAppnFwdCtrReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdCtrReset.setStatus(_A)
_NwAppnFwdCtrOperationalTime_Type=TimeTicks
_NwAppnFwdCtrOperationalTime_Object=MibScalar
nwAppnFwdCtrOperationalTime=_NwAppnFwdCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,3),_NwAppnFwdCtrOperationalTime_Type())
nwAppnFwdCtrOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrOperationalTime.setStatus(_A)
_NwAppnFwdCtrInMus_Type=Counter32
_NwAppnFwdCtrInMus_Object=MibScalar
nwAppnFwdCtrInMus=_NwAppnFwdCtrInMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,4),_NwAppnFwdCtrInMus_Type())
nwAppnFwdCtrInMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrInMus.setStatus(_A)
_NwAppnFwdCtrOutMus_Type=Counter32
_NwAppnFwdCtrOutMus_Object=MibScalar
nwAppnFwdCtrOutMus=_NwAppnFwdCtrOutMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,5),_NwAppnFwdCtrOutMus_Type())
nwAppnFwdCtrOutMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrOutMus.setStatus(_A)
_NwAppnFwdCtrFwdMus_Type=Counter32
_NwAppnFwdCtrFwdMus_Object=MibScalar
nwAppnFwdCtrFwdMus=_NwAppnFwdCtrFwdMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,6),_NwAppnFwdCtrFwdMus_Type())
nwAppnFwdCtrFwdMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrFwdMus.setStatus(_A)
_NwAppnFwdCtrFilteredMus_Type=Counter32
_NwAppnFwdCtrFilteredMus_Object=MibScalar
nwAppnFwdCtrFilteredMus=_NwAppnFwdCtrFilteredMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,7),_NwAppnFwdCtrFilteredMus_Type())
nwAppnFwdCtrFilteredMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrFilteredMus.setStatus(_A)
_NwAppnFwdCtrDiscardMus_Type=Counter32
_NwAppnFwdCtrDiscardMus_Object=MibScalar
nwAppnFwdCtrDiscardMus=_NwAppnFwdCtrDiscardMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,8),_NwAppnFwdCtrDiscardMus_Type())
nwAppnFwdCtrDiscardMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrDiscardMus.setStatus(_A)
_NwAppnFwdCtrAddrErrMus_Type=Counter32
_NwAppnFwdCtrAddrErrMus_Object=MibScalar
nwAppnFwdCtrAddrErrMus=_NwAppnFwdCtrAddrErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,9),_NwAppnFwdCtrAddrErrMus_Type())
nwAppnFwdCtrAddrErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrAddrErrMus.setStatus(_A)
_NwAppnFwdCtrLenErrMus_Type=Counter32
_NwAppnFwdCtrLenErrMus_Object=MibScalar
nwAppnFwdCtrLenErrMus=_NwAppnFwdCtrLenErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,10),_NwAppnFwdCtrLenErrMus_Type())
nwAppnFwdCtrLenErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrLenErrMus.setStatus(_A)
_NwAppnFwdCtrHdrErrMus_Type=Counter32
_NwAppnFwdCtrHdrErrMus_Object=MibScalar
nwAppnFwdCtrHdrErrMus=_NwAppnFwdCtrHdrErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,11),_NwAppnFwdCtrHdrErrMus_Type())
nwAppnFwdCtrHdrErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHdrErrMus.setStatus(_A)
_NwAppnFwdCtrInBytes_Type=Counter32
_NwAppnFwdCtrInBytes_Object=MibScalar
nwAppnFwdCtrInBytes=_NwAppnFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,12),_NwAppnFwdCtrInBytes_Type())
nwAppnFwdCtrInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrInBytes.setStatus(_A)
_NwAppnFwdCtrOutBytes_Type=Counter32
_NwAppnFwdCtrOutBytes_Object=MibScalar
nwAppnFwdCtrOutBytes=_NwAppnFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,13),_NwAppnFwdCtrOutBytes_Type())
nwAppnFwdCtrOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrOutBytes.setStatus(_A)
_NwAppnFwdCtrFwdBytes_Type=Counter32
_NwAppnFwdCtrFwdBytes_Object=MibScalar
nwAppnFwdCtrFwdBytes=_NwAppnFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,14),_NwAppnFwdCtrFwdBytes_Type())
nwAppnFwdCtrFwdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrFwdBytes.setStatus(_A)
_NwAppnFwdCtrFilteredBytes_Type=Counter32
_NwAppnFwdCtrFilteredBytes_Object=MibScalar
nwAppnFwdCtrFilteredBytes=_NwAppnFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,15),_NwAppnFwdCtrFilteredBytes_Type())
nwAppnFwdCtrFilteredBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrFilteredBytes.setStatus(_A)
_NwAppnFwdCtrDiscardBytes_Type=Counter32
_NwAppnFwdCtrDiscardBytes_Object=MibScalar
nwAppnFwdCtrDiscardBytes=_NwAppnFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,16),_NwAppnFwdCtrDiscardBytes_Type())
nwAppnFwdCtrDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrDiscardBytes.setStatus(_A)
_NwAppnFwdCtrHostInMus_Type=Counter32
_NwAppnFwdCtrHostInMus_Object=MibScalar
nwAppnFwdCtrHostInMus=_NwAppnFwdCtrHostInMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,17),_NwAppnFwdCtrHostInMus_Type())
nwAppnFwdCtrHostInMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostInMus.setStatus(_A)
_NwAppnFwdCtrHostOutMus_Type=Counter32
_NwAppnFwdCtrHostOutMus_Object=MibScalar
nwAppnFwdCtrHostOutMus=_NwAppnFwdCtrHostOutMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,18),_NwAppnFwdCtrHostOutMus_Type())
nwAppnFwdCtrHostOutMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostOutMus.setStatus(_A)
_NwAppnFwdCtrHostDiscardMus_Type=Counter32
_NwAppnFwdCtrHostDiscardMus_Object=MibScalar
nwAppnFwdCtrHostDiscardMus=_NwAppnFwdCtrHostDiscardMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,19),_NwAppnFwdCtrHostDiscardMus_Type())
nwAppnFwdCtrHostDiscardMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostDiscardMus.setStatus(_A)
_NwAppnFwdCtrHostInBytes_Type=Counter32
_NwAppnFwdCtrHostInBytes_Object=MibScalar
nwAppnFwdCtrHostInBytes=_NwAppnFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,20),_NwAppnFwdCtrHostInBytes_Type())
nwAppnFwdCtrHostInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostInBytes.setStatus(_A)
_NwAppnFwdCtrHostOutBytes_Type=Counter32
_NwAppnFwdCtrHostOutBytes_Object=MibScalar
nwAppnFwdCtrHostOutBytes=_NwAppnFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,21),_NwAppnFwdCtrHostOutBytes_Type())
nwAppnFwdCtrHostOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostOutBytes.setStatus(_A)
_NwAppnFwdCtrHostDiscardBytes_Type=Counter32
_NwAppnFwdCtrHostDiscardBytes_Object=MibScalar
nwAppnFwdCtrHostDiscardBytes=_NwAppnFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,1,1,22),_NwAppnFwdCtrHostDiscardBytes_Type())
nwAppnFwdCtrHostDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdCtrHostDiscardBytes.setStatus(_A)
_NwAppnFwdInterfaces_ObjectIdentity=ObjectIdentity
nwAppnFwdInterfaces=_NwAppnFwdInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2))
_NwAppnFwdIfConfig_ObjectIdentity=ObjectIdentity
nwAppnFwdIfConfig=_NwAppnFwdIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1))
_NwAppnFwdIfTable_Object=MibTable
nwAppnFwdIfTable=_NwAppnFwdIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1))
if mibBuilder.loadTexts:nwAppnFwdIfTable.setStatus(_A)
_NwAppnFwdIfEntry_Object=MibTableRow
nwAppnFwdIfEntry=_NwAppnFwdIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1))
nwAppnFwdIfEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:nwAppnFwdIfEntry.setStatus(_A)
_NwAppnFwdIfIndex_Type=Integer32
_NwAppnFwdIfIndex_Object=MibTableColumn
nwAppnFwdIfIndex=_NwAppnFwdIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,1),_NwAppnFwdIfIndex_Type())
nwAppnFwdIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfIndex.setStatus(_A)
class _NwAppnFwdIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_H,3)))
_NwAppnFwdIfAdminStatus_Type.__name__=_C
_NwAppnFwdIfAdminStatus_Object=MibTableColumn
nwAppnFwdIfAdminStatus=_NwAppnFwdIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,2),_NwAppnFwdIfAdminStatus_Type())
nwAppnFwdIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfAdminStatus.setStatus(_A)
class _NwAppnFwdIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3),(_O,4),(_P,5)))
_NwAppnFwdIfOperStatus_Type.__name__=_C
_NwAppnFwdIfOperStatus_Object=MibTableColumn
nwAppnFwdIfOperStatus=_NwAppnFwdIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,3),_NwAppnFwdIfOperStatus_Type())
nwAppnFwdIfOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfOperStatus.setStatus(_A)
_NwAppnFwdIfOperationalTime_Type=TimeTicks
_NwAppnFwdIfOperationalTime_Object=MibTableColumn
nwAppnFwdIfOperationalTime=_NwAppnFwdIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,4),_NwAppnFwdIfOperationalTime_Type())
nwAppnFwdIfOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfOperationalTime.setStatus(_A)
class _NwAppnFwdIfControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_NwAppnFwdIfControl_Type.__name__=_C
_NwAppnFwdIfControl_Object=MibTableColumn
nwAppnFwdIfControl=_NwAppnFwdIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,5),_NwAppnFwdIfControl_Type())
nwAppnFwdIfControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfControl.setStatus(_A)
_NwAppnFwdIfMtu_Type=Integer32
_NwAppnFwdIfMtu_Object=MibTableColumn
nwAppnFwdIfMtu=_NwAppnFwdIfMtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,6),_NwAppnFwdIfMtu_Type())
nwAppnFwdIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfMtu.setStatus(_A)
class _NwAppnFwdIfForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnFwdIfForwarding_Type.__name__=_C
_NwAppnFwdIfForwarding_Object=MibTableColumn
nwAppnFwdIfForwarding=_NwAppnFwdIfForwarding_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,7),_NwAppnFwdIfForwarding_Type())
nwAppnFwdIfForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfForwarding.setStatus(_A)
class _NwAppnFwdIfFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*((_E,1),('ethernet',2),('i8022',4),('sync',8)))
_NwAppnFwdIfFrameType_Type.__name__=_C
_NwAppnFwdIfFrameType_Object=MibTableColumn
nwAppnFwdIfFrameType=_NwAppnFwdIfFrameType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,8),_NwAppnFwdIfFrameType_Type())
nwAppnFwdIfFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfFrameType.setStatus(_A)
_NwAppnFwdIfAclIdentifier_Type=Integer32
_NwAppnFwdIfAclIdentifier_Object=MibTableColumn
nwAppnFwdIfAclIdentifier=_NwAppnFwdIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,9),_NwAppnFwdIfAclIdentifier_Type())
nwAppnFwdIfAclIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfAclIdentifier.setStatus(_A)
class _NwAppnFwdIfAclStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnFwdIfAclStatus_Type.__name__=_C
_NwAppnFwdIfAclStatus_Object=MibTableColumn
nwAppnFwdIfAclStatus=_NwAppnFwdIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,10),_NwAppnFwdIfAclStatus_Type())
nwAppnFwdIfAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfAclStatus.setStatus(_A)
class _NwAppnFwdIfCacheControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_S,3)))
_NwAppnFwdIfCacheControl_Type.__name__=_C
_NwAppnFwdIfCacheControl_Object=MibTableColumn
nwAppnFwdIfCacheControl=_NwAppnFwdIfCacheControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,11),_NwAppnFwdIfCacheControl_Type())
nwAppnFwdIfCacheControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfCacheControl.setStatus(_A)
_NwAppnFwdIfCacheEntries_Type=Counter32
_NwAppnFwdIfCacheEntries_Object=MibTableColumn
nwAppnFwdIfCacheEntries=_NwAppnFwdIfCacheEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,12),_NwAppnFwdIfCacheEntries_Type())
nwAppnFwdIfCacheEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCacheEntries.setStatus(_A)
_NwAppnFwdIfCacheHits_Type=Counter32
_NwAppnFwdIfCacheHits_Object=MibTableColumn
nwAppnFwdIfCacheHits=_NwAppnFwdIfCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,13),_NwAppnFwdIfCacheHits_Type())
nwAppnFwdIfCacheHits.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCacheHits.setStatus(_A)
_NwAppnFwdIfCacheMisses_Type=Counter32
_NwAppnFwdIfCacheMisses_Object=MibTableColumn
nwAppnFwdIfCacheMisses=_NwAppnFwdIfCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,1,1,14),_NwAppnFwdIfCacheMisses_Type())
nwAppnFwdIfCacheMisses.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCacheMisses.setStatus(_A)
_NwAppnExtensionTable_Object=MibTable
nwAppnExtensionTable=_NwAppnExtensionTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2))
if mibBuilder.loadTexts:nwAppnExtensionTable.setStatus(_A)
_NwAppnExtEntry_Object=MibTableRow
nwAppnExtEntry=_NwAppnExtEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1))
nwAppnExtEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:nwAppnExtEntry.setStatus(_A)
_NwAppnExtIfIndex_Type=Integer32
_NwAppnExtIfIndex_Object=MibTableColumn
nwAppnExtIfIndex=_NwAppnExtIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,1),_NwAppnExtIfIndex_Type())
nwAppnExtIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnExtIfIndex.setStatus(_A)
class _NwAppnExtIfPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnExtIfPortName_Type.__name__=_F
_NwAppnExtIfPortName_Object=MibTableColumn
nwAppnExtIfPortName=_NwAppnExtIfPortName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,2),_NwAppnExtIfPortName_Type())
nwAppnExtIfPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnExtIfPortName.setStatus(_A)
class _NwAppnExtIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonswitched',1),('switched',2),('satf',3)))
_NwAppnExtIfPortType_Type.__name__=_C
_NwAppnExtIfPortType_Object=MibTableColumn
nwAppnExtIfPortType=_NwAppnExtIfPortType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,4),_NwAppnExtIfPortType_Type())
nwAppnExtIfPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfPortType.setStatus(_A)
class _NwAppnExtIfDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('llc2',1),('sdlc',2),('x25',3)))
_NwAppnExtIfDlcType_Type.__name__=_C
_NwAppnExtIfDlcType_Object=MibTableColumn
nwAppnExtIfDlcType=_NwAppnExtIfDlcType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,5),_NwAppnExtIfDlcType_Type())
nwAppnExtIfDlcType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnExtIfDlcType.setStatus(_A)
class _NwAppnExtIfMaxRBtuSize_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(99,65535))
_NwAppnExtIfMaxRBtuSize_Type.__name__=_C
_NwAppnExtIfMaxRBtuSize_Object=MibTableColumn
nwAppnExtIfMaxRBtuSize=_NwAppnExtIfMaxRBtuSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,6),_NwAppnExtIfMaxRBtuSize_Type())
nwAppnExtIfMaxRBtuSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfMaxRBtuSize.setStatus(_A)
class _NwAppnExtIfTotLsActLim_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_NwAppnExtIfTotLsActLim_Type.__name__=_C
_NwAppnExtIfTotLsActLim_Object=MibTableColumn
nwAppnExtIfTotLsActLim=_NwAppnExtIfTotLsActLim_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,7),_NwAppnExtIfTotLsActLim_Type())
nwAppnExtIfTotLsActLim.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfTotLsActLim.setStatus(_A)
class _NwAppnExtIfInbLsActLim_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_NwAppnExtIfInbLsActLim_Type.__name__=_C
_NwAppnExtIfInbLsActLim_Object=MibTableColumn
nwAppnExtIfInbLsActLim=_NwAppnExtIfInbLsActLim_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,8),_NwAppnExtIfInbLsActLim_Type())
nwAppnExtIfInbLsActLim.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfInbLsActLim.setStatus(_A)
class _NwAppnExtIfOutbLsActLim_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_NwAppnExtIfOutbLsActLim_Type.__name__=_C
_NwAppnExtIfOutbLsActLim_Object=MibTableColumn
nwAppnExtIfOutbLsActLim=_NwAppnExtIfOutbLsActLim_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,9),_NwAppnExtIfOutbLsActLim_Type())
nwAppnExtIfOutbLsActLim.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfOutbLsActLim.setStatus(_A)
class _NwAppnExtIfLocalLsRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('negotiable',1),('primary',2),('secondary',3)))
_NwAppnExtIfLocalLsRole_Type.__name__=_C
_NwAppnExtIfLocalLsRole_Object=MibTableColumn
nwAppnExtIfLocalLsRole=_NwAppnExtIfLocalLsRole_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,10),_NwAppnExtIfLocalLsRole_Type())
nwAppnExtIfLocalLsRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfLocalLsRole.setStatus(_A)
class _NwAppnExtIfActXidXchgLimit_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnExtIfActXidXchgLimit_Type.__name__=_C
_NwAppnExtIfActXidXchgLimit_Object=MibTableColumn
nwAppnExtIfActXidXchgLimit=_NwAppnExtIfActXidXchgLimit_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,11),_NwAppnExtIfActXidXchgLimit_Type())
nwAppnExtIfActXidXchgLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfActXidXchgLimit.setStatus(_A)
class _NwAppnExtIfNonActXidXchgLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwAppnExtIfNonActXidXchgLimit_Type.__name__=_C
_NwAppnExtIfNonActXidXchgLimit_Object=MibTableColumn
nwAppnExtIfNonActXidXchgLimit=_NwAppnExtIfNonActXidXchgLimit_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,12),_NwAppnExtIfNonActXidXchgLimit_Type())
nwAppnExtIfNonActXidXchgLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfNonActXidXchgLimit.setStatus(_A)
class _NwAppnExtIfLsXmitRcvCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twowaysimultaneous',1),('twowayalternating',2)))
_NwAppnExtIfLsXmitRcvCap_Type.__name__=_C
_NwAppnExtIfLsXmitRcvCap_Object=MibTableColumn
nwAppnExtIfLsXmitRcvCap=_NwAppnExtIfLsXmitRcvCap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,13),_NwAppnExtIfLsXmitRcvCap_Type())
nwAppnExtIfLsXmitRcvCap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfLsXmitRcvCap.setStatus(_A)
class _NwAppnExtIfMaxIfrmRcvd_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_NwAppnExtIfMaxIfrmRcvd_Type.__name__=_C
_NwAppnExtIfMaxIfrmRcvd_Object=MibTableColumn
nwAppnExtIfMaxIfrmRcvd=_NwAppnExtIfMaxIfrmRcvd_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,14),_NwAppnExtIfMaxIfrmRcvd_Type())
nwAppnExtIfMaxIfrmRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfMaxIfrmRcvd.setStatus(_A)
class _NwAppnExtIfDfltTargetPacing_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_NwAppnExtIfDfltTargetPacing_Type.__name__=_C
_NwAppnExtIfDfltTargetPacing_Object=MibTableColumn
nwAppnExtIfDfltTargetPacing=_NwAppnExtIfDfltTargetPacing_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,15),_NwAppnExtIfDfltTargetPacing_Type())
nwAppnExtIfDfltTargetPacing.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltTargetPacing.setStatus(_A)
class _NwAppnExtIfDfltMaxSBtuSize_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(99,65535))
_NwAppnExtIfDfltMaxSBtuSize_Type.__name__=_C
_NwAppnExtIfDfltMaxSBtuSize_Object=MibTableColumn
nwAppnExtIfDfltMaxSBtuSize=_NwAppnExtIfDfltMaxSBtuSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,16),_NwAppnExtIfDfltMaxSBtuSize_Type())
nwAppnExtIfDfltMaxSBtuSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltMaxSBtuSize.setStatus(_A)
class _NwAppnExtIfDfltEffectCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,603979776))
_NwAppnExtIfDfltEffectCap_Type.__name__=_C
_NwAppnExtIfDfltEffectCap_Object=MibTableColumn
nwAppnExtIfDfltEffectCap=_NwAppnExtIfDfltEffectCap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,17),_NwAppnExtIfDfltEffectCap_Type())
nwAppnExtIfDfltEffectCap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltEffectCap.setStatus(_A)
class _NwAppnExtIfDfltConnectCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnExtIfDfltConnectCost_Type.__name__=_C
_NwAppnExtIfDfltConnectCost_Object=MibTableColumn
nwAppnExtIfDfltConnectCost=_NwAppnExtIfDfltConnectCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,18),_NwAppnExtIfDfltConnectCost_Type())
nwAppnExtIfDfltConnectCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltConnectCost.setStatus(_A)
class _NwAppnExtIfDfltByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnExtIfDfltByteCost_Type.__name__=_C
_NwAppnExtIfDfltByteCost_Object=MibTableColumn
nwAppnExtIfDfltByteCost=_NwAppnExtIfDfltByteCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,19),_NwAppnExtIfDfltByteCost_Type())
nwAppnExtIfDfltByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltByteCost.setStatus(_A)
class _NwAppnExtIfDfltSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_T,1),(_U,32),(_V,64),(_W,96),(_X,128),(_Y,160),(_Z,192)))
_NwAppnExtIfDfltSecurity_Type.__name__=_C
_NwAppnExtIfDfltSecurity_Object=MibTableColumn
nwAppnExtIfDfltSecurity=_NwAppnExtIfDfltSecurity_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,20),_NwAppnExtIfDfltSecurity_Type())
nwAppnExtIfDfltSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltSecurity.setStatus(_A)
class _NwAppnExtIfDfltPropDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_a,0),(_b,384),(_c,9216),(_d,147456),(_e,294912),(_f,2013265920)))
_NwAppnExtIfDfltPropDelay_Type.__name__=_C
_NwAppnExtIfDfltPropDelay_Object=MibTableColumn
nwAppnExtIfDfltPropDelay=_NwAppnExtIfDfltPropDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,21),_NwAppnExtIfDfltPropDelay_Type())
nwAppnExtIfDfltPropDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltPropDelay.setStatus(_A)
class _NwAppnExtIfDfltUsrDef1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnExtIfDfltUsrDef1_Type.__name__=_C
_NwAppnExtIfDfltUsrDef1_Object=MibTableColumn
nwAppnExtIfDfltUsrDef1=_NwAppnExtIfDfltUsrDef1_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,22),_NwAppnExtIfDfltUsrDef1_Type())
nwAppnExtIfDfltUsrDef1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltUsrDef1.setStatus(_A)
class _NwAppnExtIfDfltUsrDef2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnExtIfDfltUsrDef2_Type.__name__=_C
_NwAppnExtIfDfltUsrDef2_Object=MibTableColumn
nwAppnExtIfDfltUsrDef2=_NwAppnExtIfDfltUsrDef2_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,23),_NwAppnExtIfDfltUsrDef2_Type())
nwAppnExtIfDfltUsrDef2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltUsrDef2.setStatus(_A)
class _NwAppnExtIfDfltUsrDef3_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnExtIfDfltUsrDef3_Type.__name__=_C
_NwAppnExtIfDfltUsrDef3_Object=MibTableColumn
nwAppnExtIfDfltUsrDef3=_NwAppnExtIfDfltUsrDef3_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,24),_NwAppnExtIfDfltUsrDef3_Type())
nwAppnExtIfDfltUsrDef3.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfDfltUsrDef3.setStatus(_A)
class _NwAppnExtIfStopType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_l,2)))
_NwAppnExtIfStopType_Type.__name__=_C
_NwAppnExtIfStopType_Object=MibTableColumn
nwAppnExtIfStopType=_NwAppnExtIfStopType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,25),_NwAppnExtIfStopType_Type())
nwAppnExtIfStopType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfStopType.setStatus(_A)
class _NwAppnExtIfCpCpSupp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnExtIfCpCpSupp_Type.__name__=_C
_NwAppnExtIfCpCpSupp_Object=MibTableColumn
nwAppnExtIfCpCpSupp=_NwAppnExtIfCpCpSupp_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,26),_NwAppnExtIfCpCpSupp_Type())
nwAppnExtIfCpCpSupp.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfCpCpSupp.setStatus(_A)
class _NwAppnExtIfLimitedRsrc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnExtIfLimitedRsrc_Type.__name__=_C
_NwAppnExtIfLimitedRsrc_Object=MibTableColumn
nwAppnExtIfLimitedRsrc=_NwAppnExtIfLimitedRsrc_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,27),_NwAppnExtIfLimitedRsrc_Type())
nwAppnExtIfLimitedRsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfLimitedRsrc.setStatus(_A)
class _NwAppnExtIfAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NwAppnExtIfAddress_Type.__name__=_L
_NwAppnExtIfAddress_Object=MibTableColumn
nwAppnExtIfAddress=_NwAppnExtIfAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,28),_NwAppnExtIfAddress_Type())
nwAppnExtIfAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnExtIfAddress.setStatus(_A)
class _NwAppnExtIfSsap_Type(OctetString):defaultHexValue='04';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NwAppnExtIfSsap_Type.__name__=_L
_NwAppnExtIfSsap_Object=MibTableColumn
nwAppnExtIfSsap=_NwAppnExtIfSsap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,2,1,29),_NwAppnExtIfSsap_Type())
nwAppnExtIfSsap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnExtIfSsap.setStatus(_A)
_NwAppnIfCn_ObjectIdentity=ObjectIdentity
nwAppnIfCn=_NwAppnIfCn_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3))
_NwAppnIfCnPortTable_Object=MibTable
nwAppnIfCnPortTable=_NwAppnIfCnPortTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,1))
if mibBuilder.loadTexts:nwAppnIfCnPortTable.setStatus(_A)
_NwAppnIfCnPortEntry_Object=MibTableRow
nwAppnIfCnPortEntry=_NwAppnIfCnPortEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,1,1))
nwAppnIfCnPortEntry.setIndexNames((0,_G,_m),(0,_G,_n))
if mibBuilder.loadTexts:nwAppnIfCnPortEntry.setStatus(_A)
class _NwAppnIfCnPtFqName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_NwAppnIfCnPtFqName_Type.__name__=_F
_NwAppnIfCnPtFqName_Object=MibTableColumn
nwAppnIfCnPtFqName=_NwAppnIfCnPtFqName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,1,1,1),_NwAppnIfCnPtFqName_Type())
nwAppnIfCnPtFqName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnPtFqName.setStatus(_A)
class _NwAppnIfCnPtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnIfCnPtName_Type.__name__=_F
_NwAppnIfCnPtName_Object=MibTableColumn
nwAppnIfCnPtName=_NwAppnIfCnPtName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,1,1,2),_NwAppnIfCnPtName_Type())
nwAppnIfCnPtName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnPtName.setStatus(_A)
class _NwAppnIfCnPtControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_E,1),(_N,3)))
_NwAppnIfCnPtControl_Type.__name__=_C
_NwAppnIfCnPtControl_Object=MibTableColumn
nwAppnIfCnPtControl=_NwAppnIfCnPtControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,1,1,3),_NwAppnIfCnPtControl_Type())
nwAppnIfCnPtControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnPtControl.setStatus(_A)
_NwAppnIfCnTgCharTable_Object=MibTable
nwAppnIfCnTgCharTable=_NwAppnIfCnTgCharTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2))
if mibBuilder.loadTexts:nwAppnIfCnTgCharTable.setStatus(_A)
_NwAppnIfCnTgCharEntry_Object=MibTableRow
nwAppnIfCnTgCharEntry=_NwAppnIfCnTgCharEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1))
nwAppnIfCnTgCharEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:nwAppnIfCnTgCharEntry.setStatus(_A)
class _NwAppnIfCnTgFqName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_NwAppnIfCnTgFqName_Type.__name__=_F
_NwAppnIfCnTgFqName_Object=MibTableColumn
nwAppnIfCnTgFqName=_NwAppnIfCnTgFqName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,1),_NwAppnIfCnTgFqName_Type())
nwAppnIfCnTgFqName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgFqName.setStatus(_A)
class _NwAppnIfCnTgEffectCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,603979776))
_NwAppnIfCnTgEffectCap_Type.__name__=_C
_NwAppnIfCnTgEffectCap_Object=MibTableColumn
nwAppnIfCnTgEffectCap=_NwAppnIfCnTgEffectCap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,2),_NwAppnIfCnTgEffectCap_Type())
nwAppnIfCnTgEffectCap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgEffectCap.setStatus(_A)
class _NwAppnIfCnTgConnectCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnIfCnTgConnectCost_Type.__name__=_C
_NwAppnIfCnTgConnectCost_Object=MibTableColumn
nwAppnIfCnTgConnectCost=_NwAppnIfCnTgConnectCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,3),_NwAppnIfCnTgConnectCost_Type())
nwAppnIfCnTgConnectCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgConnectCost.setStatus(_A)
class _NwAppnIfCnTgByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnIfCnTgByteCost_Type.__name__=_C
_NwAppnIfCnTgByteCost_Object=MibTableColumn
nwAppnIfCnTgByteCost=_NwAppnIfCnTgByteCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,4),_NwAppnIfCnTgByteCost_Type())
nwAppnIfCnTgByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgByteCost.setStatus(_A)
class _NwAppnIfCnTgSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_T,1),(_U,32),(_V,64),(_W,96),(_X,128),(_Y,160),(_Z,192)))
_NwAppnIfCnTgSecurity_Type.__name__=_C
_NwAppnIfCnTgSecurity_Object=MibTableColumn
nwAppnIfCnTgSecurity=_NwAppnIfCnTgSecurity_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,5),_NwAppnIfCnTgSecurity_Type())
nwAppnIfCnTgSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgSecurity.setStatus(_A)
class _NwAppnIfCnTgPropDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_a,0),(_b,384),(_c,9216),(_d,147456),(_e,294912),(_f,2013265920)))
_NwAppnIfCnTgPropDelay_Type.__name__=_C
_NwAppnIfCnTgPropDelay_Object=MibTableColumn
nwAppnIfCnTgPropDelay=_NwAppnIfCnTgPropDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,6),_NwAppnIfCnTgPropDelay_Type())
nwAppnIfCnTgPropDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgPropDelay.setStatus(_A)
class _NwAppnIfCnTgUsrDef1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnIfCnTgUsrDef1_Type.__name__=_C
_NwAppnIfCnTgUsrDef1_Object=MibTableColumn
nwAppnIfCnTgUsrDef1=_NwAppnIfCnTgUsrDef1_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,7),_NwAppnIfCnTgUsrDef1_Type())
nwAppnIfCnTgUsrDef1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgUsrDef1.setStatus(_A)
class _NwAppnIfCnTgUsrDef2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnIfCnTgUsrDef2_Type.__name__=_C
_NwAppnIfCnTgUsrDef2_Object=MibTableColumn
nwAppnIfCnTgUsrDef2=_NwAppnIfCnTgUsrDef2_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,8),_NwAppnIfCnTgUsrDef2_Type())
nwAppnIfCnTgUsrDef2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgUsrDef2.setStatus(_A)
class _NwAppnIfCnTgUsrDef3_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnIfCnTgUsrDef3_Type.__name__=_C
_NwAppnIfCnTgUsrDef3_Object=MibTableColumn
nwAppnIfCnTgUsrDef3=_NwAppnIfCnTgUsrDef3_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,1,3,2,1,9),_NwAppnIfCnTgUsrDef3_Type())
nwAppnIfCnTgUsrDef3.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIfCnTgUsrDef3.setStatus(_A)
_NwAppnFwdIfCounters_ObjectIdentity=ObjectIdentity
nwAppnFwdIfCounters=_NwAppnFwdIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2))
_NwAppnFwdIfCtrTable_Object=MibTable
nwAppnFwdIfCtrTable=_NwAppnFwdIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1))
if mibBuilder.loadTexts:nwAppnFwdIfCtrTable.setStatus(_A)
_NwAppnFwdIfCtrEntry_Object=MibTableRow
nwAppnFwdIfCtrEntry=_NwAppnFwdIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1))
nwAppnFwdIfCtrEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:nwAppnFwdIfCtrEntry.setStatus(_A)
_NwAppnFwdIfCtrIfIndex_Type=Integer32
_NwAppnFwdIfCtrIfIndex_Object=MibTableColumn
nwAppnFwdIfCtrIfIndex=_NwAppnFwdIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,1),_NwAppnFwdIfCtrIfIndex_Type())
nwAppnFwdIfCtrIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrIfIndex.setStatus(_A)
class _NwAppnFwdIfCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnFwdIfCtrAdminStatus_Type.__name__=_C
_NwAppnFwdIfCtrAdminStatus_Object=MibTableColumn
nwAppnFwdIfCtrAdminStatus=_NwAppnFwdIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,2),_NwAppnFwdIfCtrAdminStatus_Type())
nwAppnFwdIfCtrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfCtrAdminStatus.setStatus(_A)
class _NwAppnFwdIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_Q,2)))
_NwAppnFwdIfCtrReset_Type.__name__=_C
_NwAppnFwdIfCtrReset_Object=MibTableColumn
nwAppnFwdIfCtrReset=_NwAppnFwdIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,3),_NwAppnFwdIfCtrReset_Type())
nwAppnFwdIfCtrReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdIfCtrReset.setStatus(_A)
_NwAppnFwdIfCtrOperationalTime_Type=TimeTicks
_NwAppnFwdIfCtrOperationalTime_Object=MibTableColumn
nwAppnFwdIfCtrOperationalTime=_NwAppnFwdIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,4),_NwAppnFwdIfCtrOperationalTime_Type())
nwAppnFwdIfCtrOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrOperationalTime.setStatus(_A)
_NwAppnFwdIfCtrInMus_Type=Counter32
_NwAppnFwdIfCtrInMus_Object=MibTableColumn
nwAppnFwdIfCtrInMus=_NwAppnFwdIfCtrInMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,5),_NwAppnFwdIfCtrInMus_Type())
nwAppnFwdIfCtrInMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrInMus.setStatus(_A)
_NwAppnFwdIfCtrOutMus_Type=Counter32
_NwAppnFwdIfCtrOutMus_Object=MibTableColumn
nwAppnFwdIfCtrOutMus=_NwAppnFwdIfCtrOutMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,6),_NwAppnFwdIfCtrOutMus_Type())
nwAppnFwdIfCtrOutMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrOutMus.setStatus(_A)
_NwAppnFwdIfCtrFwdMus_Type=Counter32
_NwAppnFwdIfCtrFwdMus_Object=MibTableColumn
nwAppnFwdIfCtrFwdMus=_NwAppnFwdIfCtrFwdMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,7),_NwAppnFwdIfCtrFwdMus_Type())
nwAppnFwdIfCtrFwdMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrFwdMus.setStatus(_A)
_NwAppnFwdIfCtrFilteredMus_Type=Counter32
_NwAppnFwdIfCtrFilteredMus_Object=MibTableColumn
nwAppnFwdIfCtrFilteredMus=_NwAppnFwdIfCtrFilteredMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,8),_NwAppnFwdIfCtrFilteredMus_Type())
nwAppnFwdIfCtrFilteredMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrFilteredMus.setStatus(_A)
_NwAppnFwdIfCtrDiscardMus_Type=Counter32
_NwAppnFwdIfCtrDiscardMus_Object=MibTableColumn
nwAppnFwdIfCtrDiscardMus=_NwAppnFwdIfCtrDiscardMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,9),_NwAppnFwdIfCtrDiscardMus_Type())
nwAppnFwdIfCtrDiscardMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrDiscardMus.setStatus(_A)
_NwAppnFwdIfCtrAddrErrMus_Type=Counter32
_NwAppnFwdIfCtrAddrErrMus_Object=MibTableColumn
nwAppnFwdIfCtrAddrErrMus=_NwAppnFwdIfCtrAddrErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,10),_NwAppnFwdIfCtrAddrErrMus_Type())
nwAppnFwdIfCtrAddrErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrAddrErrMus.setStatus(_A)
_NwAppnFwdIfCtrLenErrMus_Type=Counter32
_NwAppnFwdIfCtrLenErrMus_Object=MibTableColumn
nwAppnFwdIfCtrLenErrMus=_NwAppnFwdIfCtrLenErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,11),_NwAppnFwdIfCtrLenErrMus_Type())
nwAppnFwdIfCtrLenErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrLenErrMus.setStatus(_A)
_NwAppnFwdIfCtrHdrErrMus_Type=Counter32
_NwAppnFwdIfCtrHdrErrMus_Object=MibTableColumn
nwAppnFwdIfCtrHdrErrMus=_NwAppnFwdIfCtrHdrErrMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,12),_NwAppnFwdIfCtrHdrErrMus_Type())
nwAppnFwdIfCtrHdrErrMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHdrErrMus.setStatus(_A)
_NwAppnFwdIfCtrInBytes_Type=Counter32
_NwAppnFwdIfCtrInBytes_Object=MibTableColumn
nwAppnFwdIfCtrInBytes=_NwAppnFwdIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,13),_NwAppnFwdIfCtrInBytes_Type())
nwAppnFwdIfCtrInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrInBytes.setStatus(_A)
_NwAppnFwdIfCtrOutBytes_Type=Counter32
_NwAppnFwdIfCtrOutBytes_Object=MibTableColumn
nwAppnFwdIfCtrOutBytes=_NwAppnFwdIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,14),_NwAppnFwdIfCtrOutBytes_Type())
nwAppnFwdIfCtrOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrOutBytes.setStatus(_A)
_NwAppnFwdIfCtrFwdBytes_Type=Counter32
_NwAppnFwdIfCtrFwdBytes_Object=MibTableColumn
nwAppnFwdIfCtrFwdBytes=_NwAppnFwdIfCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,15),_NwAppnFwdIfCtrFwdBytes_Type())
nwAppnFwdIfCtrFwdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrFwdBytes.setStatus(_A)
_NwAppnFwdIfCtrFilteredBytes_Type=Counter32
_NwAppnFwdIfCtrFilteredBytes_Object=MibTableColumn
nwAppnFwdIfCtrFilteredBytes=_NwAppnFwdIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,16),_NwAppnFwdIfCtrFilteredBytes_Type())
nwAppnFwdIfCtrFilteredBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrFilteredBytes.setStatus(_A)
_NwAppnFwdIfCtrDiscardBytes_Type=Counter32
_NwAppnFwdIfCtrDiscardBytes_Object=MibTableColumn
nwAppnFwdIfCtrDiscardBytes=_NwAppnFwdIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,17),_NwAppnFwdIfCtrDiscardBytes_Type())
nwAppnFwdIfCtrDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrDiscardBytes.setStatus(_A)
_NwAppnFwdIfCtrHostInMus_Type=Counter32
_NwAppnFwdIfCtrHostInMus_Object=MibTableColumn
nwAppnFwdIfCtrHostInMus=_NwAppnFwdIfCtrHostInMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,18),_NwAppnFwdIfCtrHostInMus_Type())
nwAppnFwdIfCtrHostInMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostInMus.setStatus(_A)
_NwAppnFwdIfCtrHostOutMus_Type=Counter32
_NwAppnFwdIfCtrHostOutMus_Object=MibTableColumn
nwAppnFwdIfCtrHostOutMus=_NwAppnFwdIfCtrHostOutMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,19),_NwAppnFwdIfCtrHostOutMus_Type())
nwAppnFwdIfCtrHostOutMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostOutMus.setStatus(_A)
_NwAppnFwdIfCtrHostDiscardMus_Type=Counter32
_NwAppnFwdIfCtrHostDiscardMus_Object=MibTableColumn
nwAppnFwdIfCtrHostDiscardMus=_NwAppnFwdIfCtrHostDiscardMus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,20),_NwAppnFwdIfCtrHostDiscardMus_Type())
nwAppnFwdIfCtrHostDiscardMus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostDiscardMus.setStatus(_A)
_NwAppnFwdIfCtrHostInBytes_Type=Counter32
_NwAppnFwdIfCtrHostInBytes_Object=MibTableColumn
nwAppnFwdIfCtrHostInBytes=_NwAppnFwdIfCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,21),_NwAppnFwdIfCtrHostInBytes_Type())
nwAppnFwdIfCtrHostInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostInBytes.setStatus(_A)
_NwAppnFwdIfCtrHostOutBytes_Type=Counter32
_NwAppnFwdIfCtrHostOutBytes_Object=MibTableColumn
nwAppnFwdIfCtrHostOutBytes=_NwAppnFwdIfCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,22),_NwAppnFwdIfCtrHostOutBytes_Type())
nwAppnFwdIfCtrHostOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostOutBytes.setStatus(_A)
_NwAppnFwdIfCtrHostDiscardBytes_Type=Counter32
_NwAppnFwdIfCtrHostDiscardBytes_Object=MibTableColumn
nwAppnFwdIfCtrHostDiscardBytes=_NwAppnFwdIfCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,2,2,1,1,23),_NwAppnFwdIfCtrHostDiscardBytes_Type())
nwAppnFwdIfCtrHostDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdIfCtrHostDiscardBytes.setStatus(_A)
_NwAppnFwdLinks_ObjectIdentity=ObjectIdentity
nwAppnFwdLinks=_NwAppnFwdLinks_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3))
_NwAppnFwdLsConfig_ObjectIdentity=ObjectIdentity
nwAppnFwdLsConfig=_NwAppnFwdLsConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1))
_NwAppnFwdLsTable_Object=MibTable
nwAppnFwdLsTable=_NwAppnFwdLsTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1))
if mibBuilder.loadTexts:nwAppnFwdLsTable.setStatus(_A)
_NwAppnFwdLsEntry_Object=MibTableRow
nwAppnFwdLsEntry=_NwAppnFwdLsEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1))
nwAppnFwdLsEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:nwAppnFwdLsEntry.setStatus(_A)
class _NwAppnFwdLsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnFwdLsName_Type.__name__=_F
_NwAppnFwdLsName_Object=MibTableColumn
nwAppnFwdLsName=_NwAppnFwdLsName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,1),_NwAppnFwdLsName_Type())
nwAppnFwdLsName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsName.setStatus(_A)
class _NwAppnFwdLsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_S,3)))
_NwAppnFwdLsAdminStatus_Type.__name__=_C
_NwAppnFwdLsAdminStatus_Object=MibTableColumn
nwAppnFwdLsAdminStatus=_NwAppnFwdLsAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,2),_NwAppnFwdLsAdminStatus_Type())
nwAppnFwdLsAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsAdminStatus.setStatus(_A)
class _NwAppnFwdLsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3),(_O,4),(_P,5)))
_NwAppnFwdLsOperStatus_Type.__name__=_C
_NwAppnFwdLsOperStatus_Object=MibTableColumn
nwAppnFwdLsOperStatus=_NwAppnFwdLsOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,3),_NwAppnFwdLsOperStatus_Type())
nwAppnFwdLsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsOperStatus.setStatus(_A)
_NwAppnFwdLsOperationalTime_Type=TimeTicks
_NwAppnFwdLsOperationalTime_Object=MibTableColumn
nwAppnFwdLsOperationalTime=_NwAppnFwdLsOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,4),_NwAppnFwdLsOperationalTime_Type())
nwAppnFwdLsOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsOperationalTime.setStatus(_A)
class _NwAppnFwdLsControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_E,1),(_N,3)))
_NwAppnFwdLsControl_Type.__name__=_C
_NwAppnFwdLsControl_Object=MibTableColumn
nwAppnFwdLsControl=_NwAppnFwdLsControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,5),_NwAppnFwdLsControl_Type())
nwAppnFwdLsControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsControl.setStatus(_A)
class _NwAppnFwdLsPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnFwdLsPortName_Type.__name__=_F
_NwAppnFwdLsPortName_Object=MibTableColumn
nwAppnFwdLsPortName=_NwAppnFwdLsPortName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,6),_NwAppnFwdLsPortName_Type())
nwAppnFwdLsPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsPortName.setStatus(_A)
class _NwAppnFwdLsAdjCpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_NwAppnFwdLsAdjCpName_Type.__name__=_F
_NwAppnFwdLsAdjCpName_Object=MibTableColumn
nwAppnFwdLsAdjCpName=_NwAppnFwdLsAdjCpName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,7),_NwAppnFwdLsAdjCpName_Type())
nwAppnFwdLsAdjCpName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsAdjCpName.setStatus(_A)
class _NwAppnFwdLsAdjCpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('endnode',1),(_g,2)))
_NwAppnFwdLsAdjCpType_Type.__name__=_C
_NwAppnFwdLsAdjCpType_Object=MibTableColumn
nwAppnFwdLsAdjCpType=_NwAppnFwdLsAdjCpType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,8),_NwAppnFwdLsAdjCpType_Type())
nwAppnFwdLsAdjCpType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsAdjCpType.setStatus(_A)
class _NwAppnFwdLsAutoActSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnFwdLsAutoActSupport_Type.__name__=_C
_NwAppnFwdLsAutoActSupport_Object=MibTableColumn
nwAppnFwdLsAutoActSupport=_NwAppnFwdLsAutoActSupport_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,10),_NwAppnFwdLsAutoActSupport_Type())
nwAppnFwdLsAutoActSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsAutoActSupport.setStatus(_A)
class _NwAppnFwdLsLimitedRsrc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnFwdLsLimitedRsrc_Type.__name__=_C
_NwAppnFwdLsLimitedRsrc_Object=MibTableColumn
nwAppnFwdLsLimitedRsrc=_NwAppnFwdLsLimitedRsrc_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,11),_NwAppnFwdLsLimitedRsrc_Type())
nwAppnFwdLsLimitedRsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsLimitedRsrc.setStatus(_A)
class _NwAppnFwdLsSscpSession_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnFwdLsSscpSession_Type.__name__=_C
_NwAppnFwdLsSscpSession_Object=MibTableColumn
nwAppnFwdLsSscpSession=_NwAppnFwdLsSscpSession_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,12),_NwAppnFwdLsSscpSession_Type())
nwAppnFwdLsSscpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsSscpSession.setStatus(_A)
class _NwAppnFwdLsPuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnFwdLsPuName_Type.__name__=_F
_NwAppnFwdLsPuName_Object=MibTableColumn
nwAppnFwdLsPuName=_NwAppnFwdLsPuName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,13),_NwAppnFwdLsPuName_Type())
nwAppnFwdLsPuName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsPuName.setStatus(_A)
class _NwAppnFwdLsBackLvlLenEN_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('xid3',2),('xid0',3),('noxid',4)))
_NwAppnFwdLsBackLvlLenEN_Type.__name__=_C
_NwAppnFwdLsBackLvlLenEN_Object=MibTableColumn
nwAppnFwdLsBackLvlLenEN=_NwAppnFwdLsBackLvlLenEN_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,14),_NwAppnFwdLsBackLvlLenEN_Type())
nwAppnFwdLsBackLvlLenEN.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsBackLvlLenEN.setStatus(_A)
class _NwAppnFwdLsCpCpSessSupp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnFwdLsCpCpSessSupp_Type.__name__=_C
_NwAppnFwdLsCpCpSessSupp_Object=MibTableColumn
nwAppnFwdLsCpCpSessSupp=_NwAppnFwdLsCpCpSessSupp_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,16),_NwAppnFwdLsCpCpSessSupp_Type())
nwAppnFwdLsCpCpSessSupp.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsCpCpSessSupp.setStatus(_A)
class _NwAppnFwdLsEffectCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,603979776))
_NwAppnFwdLsEffectCap_Type.__name__=_C
_NwAppnFwdLsEffectCap_Object=MibTableColumn
nwAppnFwdLsEffectCap=_NwAppnFwdLsEffectCap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,17),_NwAppnFwdLsEffectCap_Type())
nwAppnFwdLsEffectCap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsEffectCap.setStatus(_A)
class _NwAppnFwdLsConnectCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnFwdLsConnectCost_Type.__name__=_C
_NwAppnFwdLsConnectCost_Object=MibTableColumn
nwAppnFwdLsConnectCost=_NwAppnFwdLsConnectCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,18),_NwAppnFwdLsConnectCost_Type())
nwAppnFwdLsConnectCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsConnectCost.setStatus(_A)
class _NwAppnFwdLsByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnFwdLsByteCost_Type.__name__=_C
_NwAppnFwdLsByteCost_Object=MibTableColumn
nwAppnFwdLsByteCost=_NwAppnFwdLsByteCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,19),_NwAppnFwdLsByteCost_Type())
nwAppnFwdLsByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsByteCost.setStatus(_A)
class _NwAppnFwdLsSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_T,1),(_U,32),(_V,64),(_W,96),(_X,128),(_Y,160),(_Z,192)))
_NwAppnFwdLsSecurity_Type.__name__=_C
_NwAppnFwdLsSecurity_Object=MibTableColumn
nwAppnFwdLsSecurity=_NwAppnFwdLsSecurity_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,20),_NwAppnFwdLsSecurity_Type())
nwAppnFwdLsSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsSecurity.setStatus(_A)
class _NwAppnFwdLsPropDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_a,0),(_b,384),(_c,9216),(_d,147456),(_e,294912),(_f,2013265920)))
_NwAppnFwdLsPropDelay_Type.__name__=_C
_NwAppnFwdLsPropDelay_Object=MibTableColumn
nwAppnFwdLsPropDelay=_NwAppnFwdLsPropDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,21),_NwAppnFwdLsPropDelay_Type())
nwAppnFwdLsPropDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsPropDelay.setStatus(_A)
class _NwAppnFwdLsUsrDef1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnFwdLsUsrDef1_Type.__name__=_C
_NwAppnFwdLsUsrDef1_Object=MibTableColumn
nwAppnFwdLsUsrDef1=_NwAppnFwdLsUsrDef1_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,22),_NwAppnFwdLsUsrDef1_Type())
nwAppnFwdLsUsrDef1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsUsrDef1.setStatus(_A)
class _NwAppnFwdLsUsrDef2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnFwdLsUsrDef2_Type.__name__=_C
_NwAppnFwdLsUsrDef2_Object=MibTableColumn
nwAppnFwdLsUsrDef2=_NwAppnFwdLsUsrDef2_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,23),_NwAppnFwdLsUsrDef2_Type())
nwAppnFwdLsUsrDef2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsUsrDef2.setStatus(_A)
class _NwAppnFwdLsUsrDef3_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwAppnFwdLsUsrDef3_Type.__name__=_C
_NwAppnFwdLsUsrDef3_Object=MibTableColumn
nwAppnFwdLsUsrDef3=_NwAppnFwdLsUsrDef3_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,24),_NwAppnFwdLsUsrDef3_Type())
nwAppnFwdLsUsrDef3.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsUsrDef3.setStatus(_A)
class _NwAppnFwdLsTrgtPacingCount_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_NwAppnFwdLsTrgtPacingCount_Type.__name__=_C
_NwAppnFwdLsTrgtPacingCount_Object=MibTableColumn
nwAppnFwdLsTrgtPacingCount=_NwAppnFwdLsTrgtPacingCount_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,25),_NwAppnFwdLsTrgtPacingCount_Type())
nwAppnFwdLsTrgtPacingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsTrgtPacingCount.setStatus(_A)
class _NwAppnFwdLsMaxSendBtu_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(99,65535))
_NwAppnFwdLsMaxSendBtu_Type.__name__=_C
_NwAppnFwdLsMaxSendBtu_Object=MibTableColumn
nwAppnFwdLsMaxSendBtu=_NwAppnFwdLsMaxSendBtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,26),_NwAppnFwdLsMaxSendBtu_Type())
nwAppnFwdLsMaxSendBtu.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsMaxSendBtu.setStatus(_A)
_NwAppnFwdLsNumActiveSession_Type=Integer32
_NwAppnFwdLsNumActiveSession_Object=MibTableColumn
nwAppnFwdLsNumActiveSession=_NwAppnFwdLsNumActiveSession_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,27),_NwAppnFwdLsNumActiveSession_Type())
nwAppnFwdLsNumActiveSession.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsNumActiveSession.setStatus(_A)
class _NwAppnFwdLsdynamicLs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_NwAppnFwdLsdynamicLs_Type.__name__=_C
_NwAppnFwdLsdynamicLs_Object=MibTableColumn
nwAppnFwdLsdynamicLs=_NwAppnFwdLsdynamicLs_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,28),_NwAppnFwdLsdynamicLs_Type())
nwAppnFwdLsdynamicLs.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsdynamicLs.setStatus(_A)
class _NwAppnFwdLsStopType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_l,2)))
_NwAppnFwdLsStopType_Type.__name__=_C
_NwAppnFwdLsStopType_Object=MibTableColumn
nwAppnFwdLsStopType=_NwAppnFwdLsStopType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,29),_NwAppnFwdLsStopType_Type())
nwAppnFwdLsStopType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsStopType.setStatus(_A)
_NwAppnFwdLsPortNbr_Type=Integer32
_NwAppnFwdLsPortNbr_Object=MibTableColumn
nwAppnFwdLsPortNbr=_NwAppnFwdLsPortNbr_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,30),_NwAppnFwdLsPortNbr_Type())
nwAppnFwdLsPortNbr.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsPortNbr.setStatus(_A)
class _NwAppnFwdLsDestAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NwAppnFwdLsDestAddr_Type.__name__=_L
_NwAppnFwdLsDestAddr_Object=MibTableColumn
nwAppnFwdLsDestAddr=_NwAppnFwdLsDestAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,31),_NwAppnFwdLsDestAddr_Type())
nwAppnFwdLsDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsDestAddr.setStatus(_A)
class _NwAppnFwdLsDsap_Type(OctetString):defaultHexValue='04';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NwAppnFwdLsDsap_Type.__name__=_L
_NwAppnFwdLsDsap_Object=MibTableColumn
nwAppnFwdLsDsap=_NwAppnFwdLsDsap_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,32),_NwAppnFwdLsDsap_Type())
nwAppnFwdLsDsap.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsDsap.setStatus(_A)
class _NwAppnFwdLsBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NwAppnFwdLsBlockNum_Type.__name__=_F
_NwAppnFwdLsBlockNum_Object=MibTableColumn
nwAppnFwdLsBlockNum=_NwAppnFwdLsBlockNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,33),_NwAppnFwdLsBlockNum_Type())
nwAppnFwdLsBlockNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsBlockNum.setStatus(_A)
class _NwAppnFwdLsIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_NwAppnFwdLsIdNum_Type.__name__=_F
_NwAppnFwdLsIdNum_Object=MibTableColumn
nwAppnFwdLsIdNum=_NwAppnFwdLsIdNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,1,1,1,34),_NwAppnFwdLsIdNum_Type())
nwAppnFwdLsIdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsIdNum.setStatus(_A)
_NwAppnFwdLsCounters_ObjectIdentity=ObjectIdentity
nwAppnFwdLsCounters=_NwAppnFwdLsCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2))
_NwAppnFwdLsCtrTable_Object=MibTable
nwAppnFwdLsCtrTable=_NwAppnFwdLsCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1))
if mibBuilder.loadTexts:nwAppnFwdLsCtrTable.setStatus(_A)
_NwAppnFwdLsCtrEntry_Object=MibTableRow
nwAppnFwdLsCtrEntry=_NwAppnFwdLsCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1))
nwAppnFwdLsCtrEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:nwAppnFwdLsCtrEntry.setStatus(_A)
class _NwAppnFwdLsCtrLsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NwAppnFwdLsCtrLsName_Type.__name__=_F
_NwAppnFwdLsCtrLsName_Object=MibTableColumn
nwAppnFwdLsCtrLsName=_NwAppnFwdLsCtrLsName_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,1),_NwAppnFwdLsCtrLsName_Type())
nwAppnFwdLsCtrLsName.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrLsName.setStatus(_A)
class _NwAppnFwdLsCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnFwdLsCtrAdminStatus_Type.__name__=_C
_NwAppnFwdLsCtrAdminStatus_Object=MibTableColumn
nwAppnFwdLsCtrAdminStatus=_NwAppnFwdLsCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,2),_NwAppnFwdLsCtrAdminStatus_Type())
nwAppnFwdLsCtrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsCtrAdminStatus.setStatus(_A)
class _NwAppnFwdLsCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_Q,2)))
_NwAppnFwdLsCtrReset_Type.__name__=_C
_NwAppnFwdLsCtrReset_Object=MibTableColumn
nwAppnFwdLsCtrReset=_NwAppnFwdLsCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,3),_NwAppnFwdLsCtrReset_Type())
nwAppnFwdLsCtrReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnFwdLsCtrReset.setStatus(_A)
_NwAppnFwdLsCtrOperationalTime_Type=TimeTicks
_NwAppnFwdLsCtrOperationalTime_Object=MibTableColumn
nwAppnFwdLsCtrOperationalTime=_NwAppnFwdLsCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,4),_NwAppnFwdLsCtrOperationalTime_Type())
nwAppnFwdLsCtrOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrOperationalTime.setStatus(_A)
_NwAppnFwdLsCtrInBlus_Type=Counter32
_NwAppnFwdLsCtrInBlus_Object=MibTableColumn
nwAppnFwdLsCtrInBlus=_NwAppnFwdLsCtrInBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,5),_NwAppnFwdLsCtrInBlus_Type())
nwAppnFwdLsCtrInBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrInBlus.setStatus(_A)
_NwAppnFwdLsCtrOutBlus_Type=Counter32
_NwAppnFwdLsCtrOutBlus_Object=MibTableColumn
nwAppnFwdLsCtrOutBlus=_NwAppnFwdLsCtrOutBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,6),_NwAppnFwdLsCtrOutBlus_Type())
nwAppnFwdLsCtrOutBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrOutBlus.setStatus(_A)
_NwAppnFwdLsCtrFwdBlus_Type=Counter32
_NwAppnFwdLsCtrFwdBlus_Object=MibTableColumn
nwAppnFwdLsCtrFwdBlus=_NwAppnFwdLsCtrFwdBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,7),_NwAppnFwdLsCtrFwdBlus_Type())
nwAppnFwdLsCtrFwdBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrFwdBlus.setStatus(_A)
_NwAppnFwdLsCtrFilteredBlus_Type=Counter32
_NwAppnFwdLsCtrFilteredBlus_Object=MibTableColumn
nwAppnFwdLsCtrFilteredBlus=_NwAppnFwdLsCtrFilteredBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,8),_NwAppnFwdLsCtrFilteredBlus_Type())
nwAppnFwdLsCtrFilteredBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrFilteredBlus.setStatus(_A)
_NwAppnFwdLsCtrDiscardBlus_Type=Counter32
_NwAppnFwdLsCtrDiscardBlus_Object=MibTableColumn
nwAppnFwdLsCtrDiscardBlus=_NwAppnFwdLsCtrDiscardBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,9),_NwAppnFwdLsCtrDiscardBlus_Type())
nwAppnFwdLsCtrDiscardBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrDiscardBlus.setStatus(_A)
_NwAppnFwdLsCtrAddrErrBlus_Type=Counter32
_NwAppnFwdLsCtrAddrErrBlus_Object=MibTableColumn
nwAppnFwdLsCtrAddrErrBlus=_NwAppnFwdLsCtrAddrErrBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,10),_NwAppnFwdLsCtrAddrErrBlus_Type())
nwAppnFwdLsCtrAddrErrBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrAddrErrBlus.setStatus(_A)
_NwAppnFwdLsCtrLenErrBlus_Type=Counter32
_NwAppnFwdLsCtrLenErrBlus_Object=MibTableColumn
nwAppnFwdLsCtrLenErrBlus=_NwAppnFwdLsCtrLenErrBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,11),_NwAppnFwdLsCtrLenErrBlus_Type())
nwAppnFwdLsCtrLenErrBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrLenErrBlus.setStatus(_A)
_NwAppnFwdLsCtrHdrErrBlus_Type=Counter32
_NwAppnFwdLsCtrHdrErrBlus_Object=MibTableColumn
nwAppnFwdLsCtrHdrErrBlus=_NwAppnFwdLsCtrHdrErrBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,12),_NwAppnFwdLsCtrHdrErrBlus_Type())
nwAppnFwdLsCtrHdrErrBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHdrErrBlus.setStatus(_A)
_NwAppnFwdLsCtrInBytes_Type=Counter32
_NwAppnFwdLsCtrInBytes_Object=MibTableColumn
nwAppnFwdLsCtrInBytes=_NwAppnFwdLsCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,13),_NwAppnFwdLsCtrInBytes_Type())
nwAppnFwdLsCtrInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrInBytes.setStatus(_A)
_NwAppnFwdLsCtrOutBytes_Type=Counter32
_NwAppnFwdLsCtrOutBytes_Object=MibTableColumn
nwAppnFwdLsCtrOutBytes=_NwAppnFwdLsCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,14),_NwAppnFwdLsCtrOutBytes_Type())
nwAppnFwdLsCtrOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrOutBytes.setStatus(_A)
_NwAppnFwdLsCtrFwdBytes_Type=Counter32
_NwAppnFwdLsCtrFwdBytes_Object=MibTableColumn
nwAppnFwdLsCtrFwdBytes=_NwAppnFwdLsCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,15),_NwAppnFwdLsCtrFwdBytes_Type())
nwAppnFwdLsCtrFwdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrFwdBytes.setStatus(_A)
_NwAppnFwdLsCtrFilteredBytes_Type=Counter32
_NwAppnFwdLsCtrFilteredBytes_Object=MibTableColumn
nwAppnFwdLsCtrFilteredBytes=_NwAppnFwdLsCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,16),_NwAppnFwdLsCtrFilteredBytes_Type())
nwAppnFwdLsCtrFilteredBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrFilteredBytes.setStatus(_A)
_NwAppnFwdLsCtrDiscardBytes_Type=Counter32
_NwAppnFwdLsCtrDiscardBytes_Object=MibTableColumn
nwAppnFwdLsCtrDiscardBytes=_NwAppnFwdLsCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,17),_NwAppnFwdLsCtrDiscardBytes_Type())
nwAppnFwdLsCtrDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrDiscardBytes.setStatus(_A)
_NwAppnFwdLsCtrHostInBlus_Type=Counter32
_NwAppnFwdLsCtrHostInBlus_Object=MibTableColumn
nwAppnFwdLsCtrHostInBlus=_NwAppnFwdLsCtrHostInBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,18),_NwAppnFwdLsCtrHostInBlus_Type())
nwAppnFwdLsCtrHostInBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostInBlus.setStatus(_A)
_NwAppnFwdLsCtrHostOutBlus_Type=Counter32
_NwAppnFwdLsCtrHostOutBlus_Object=MibTableColumn
nwAppnFwdLsCtrHostOutBlus=_NwAppnFwdLsCtrHostOutBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,19),_NwAppnFwdLsCtrHostOutBlus_Type())
nwAppnFwdLsCtrHostOutBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostOutBlus.setStatus(_A)
_NwAppnFwdLsCtrHostDiscardBlus_Type=Counter32
_NwAppnFwdLsCtrHostDiscardBlus_Object=MibTableColumn
nwAppnFwdLsCtrHostDiscardBlus=_NwAppnFwdLsCtrHostDiscardBlus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,20),_NwAppnFwdLsCtrHostDiscardBlus_Type())
nwAppnFwdLsCtrHostDiscardBlus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostDiscardBlus.setStatus(_A)
_NwAppnFwdLsCtrHostInBytes_Type=Counter32
_NwAppnFwdLsCtrHostInBytes_Object=MibTableColumn
nwAppnFwdLsCtrHostInBytes=_NwAppnFwdLsCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,21),_NwAppnFwdLsCtrHostInBytes_Type())
nwAppnFwdLsCtrHostInBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostInBytes.setStatus(_A)
_NwAppnFwdLsCtrHostOutBytes_Type=Counter32
_NwAppnFwdLsCtrHostOutBytes_Object=MibTableColumn
nwAppnFwdLsCtrHostOutBytes=_NwAppnFwdLsCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,22),_NwAppnFwdLsCtrHostOutBytes_Type())
nwAppnFwdLsCtrHostOutBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostOutBytes.setStatus(_A)
_NwAppnFwdLsCtrHostDiscardBytes_Type=Counter32
_NwAppnFwdLsCtrHostDiscardBytes_Object=MibTableColumn
nwAppnFwdLsCtrHostDiscardBytes=_NwAppnFwdLsCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,2,3,2,1,1,23),_NwAppnFwdLsCtrHostDiscardBytes_Type())
nwAppnFwdLsCtrHostDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnFwdLsCtrHostDiscardBytes.setStatus(_A)
_NwAppnTopology_ObjectIdentity=ObjectIdentity
nwAppnTopology=_NwAppnTopology_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4))
_NwAppnDistanceVector_ObjectIdentity=ObjectIdentity
nwAppnDistanceVector=_NwAppnDistanceVector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,1))
_NwAppnLinkState_ObjectIdentity=ObjectIdentity
nwAppnLinkState=_NwAppnLinkState_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2))
_NwAppnIsr_ObjectIdentity=ObjectIdentity
nwAppnIsr=_NwAppnIsr_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1))
_NwAppnIsrSystem_ObjectIdentity=ObjectIdentity
nwAppnIsrSystem=_NwAppnIsrSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1))
_NwAppnIsrConfig_ObjectIdentity=ObjectIdentity
nwAppnIsrConfig=_NwAppnIsrConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1))
class _NwAppnIsrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_S,3)))
_NwAppnIsrAdminStatus_Type.__name__=_C
_NwAppnIsrAdminStatus_Object=MibScalar
nwAppnIsrAdminStatus=_NwAppnIsrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1,1),_NwAppnIsrAdminStatus_Type())
nwAppnIsrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnIsrAdminStatus.setStatus(_A)
class _NwAppnIsrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3),(_O,4),(_P,5)))
_NwAppnIsrOperStatus_Type.__name__=_C
_NwAppnIsrOperStatus_Object=MibScalar
nwAppnIsrOperStatus=_NwAppnIsrOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1,2),_NwAppnIsrOperStatus_Type())
nwAppnIsrOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnIsrOperStatus.setStatus(_A)
class _NwAppnIsrAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_NwAppnIsrAdminReset_Type.__name__=_C
_NwAppnIsrAdminReset_Object=MibScalar
nwAppnIsrAdminReset=_NwAppnIsrAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1,3),_NwAppnIsrAdminReset_Type())
nwAppnIsrAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnIsrAdminReset.setStatus(_A)
_NwAppnIsrOperationalTime_Type=TimeTicks
_NwAppnIsrOperationalTime_Object=MibScalar
nwAppnIsrOperationalTime=_NwAppnIsrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1,4),_NwAppnIsrOperationalTime_Type())
nwAppnIsrOperationalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnIsrOperationalTime.setStatus(_A)
_NwAppnIsrVersion_Type=DisplayString
_NwAppnIsrVersion_Object=MibScalar
nwAppnIsrVersion=_NwAppnIsrVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,1,5),_NwAppnIsrVersion_Type())
nwAppnIsrVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnIsrVersion.setStatus(_A)
_NwAppnIsrCounters_ObjectIdentity=ObjectIdentity
nwAppnIsrCounters=_NwAppnIsrCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,1,2))
_NwAppnIsrInterfaces_ObjectIdentity=ObjectIdentity
nwAppnIsrInterfaces=_NwAppnIsrInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,2))
_NwAppnIsrIfConfig_ObjectIdentity=ObjectIdentity
nwAppnIsrIfConfig=_NwAppnIsrIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,2,1))
_NwAppnIsrIfCounters_ObjectIdentity=ObjectIdentity
nwAppnIsrIfCounters=_NwAppnIsrIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,2,2))
_NwAppnIsrDatabase_ObjectIdentity=ObjectIdentity
nwAppnIsrDatabase=_NwAppnIsrDatabase_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,3))
_NwAppnIsrFilters_ObjectIdentity=ObjectIdentity
nwAppnIsrFilters=_NwAppnIsrFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,4,2,1,4))
_NwAppnFib_ObjectIdentity=ObjectIdentity
nwAppnFib=_NwAppnFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,5))
_NwAppnEndSystems_ObjectIdentity=ObjectIdentity
nwAppnEndSystems=_NwAppnEndSystems_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,6))
_NwAppnHostsSystem_ObjectIdentity=ObjectIdentity
nwAppnHostsSystem=_NwAppnHostsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,6,1))
_NwAppnHostsInterfaces_ObjectIdentity=ObjectIdentity
nwAppnHostsInterfaces=_NwAppnHostsInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,6,2))
_NwAppnAccessControl_ObjectIdentity=ObjectIdentity
nwAppnAccessControl=_NwAppnAccessControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,7))
_NwAppnFilters_ObjectIdentity=ObjectIdentity
nwAppnFilters=_NwAppnFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,8))
_NwAppnRedirector_ObjectIdentity=ObjectIdentity
nwAppnRedirector=_NwAppnRedirector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,9))
_NwAppnEvent_ObjectIdentity=ObjectIdentity
nwAppnEvent=_NwAppnEvent_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10))
_NwAppnEventLogConfig_ObjectIdentity=ObjectIdentity
nwAppnEventLogConfig=_NwAppnEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,1))
class _NwAppnEventAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnEventAdminStatus_Type.__name__=_C
_NwAppnEventAdminStatus_Object=MibScalar
nwAppnEventAdminStatus=_NwAppnEventAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,1,1),_NwAppnEventAdminStatus_Type())
nwAppnEventAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventAdminStatus.setStatus(_A)
_NwAppnEventMaxEntries_Type=Integer32
_NwAppnEventMaxEntries_Object=MibScalar
nwAppnEventMaxEntries=_NwAppnEventMaxEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,1,2),_NwAppnEventMaxEntries_Type())
nwAppnEventMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventMaxEntries.setStatus(_A)
class _NwAppnEventTraceAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_H,3)))
_NwAppnEventTraceAll_Type.__name__=_C
_NwAppnEventTraceAll_Object=MibScalar
nwAppnEventTraceAll=_NwAppnEventTraceAll_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,1,3),_NwAppnEventTraceAll_Type())
nwAppnEventTraceAll.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventTraceAll.setStatus(_A)
_NwAppnEventLogFilterTable_ObjectIdentity=ObjectIdentity
nwAppnEventLogFilterTable=_NwAppnEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2))
_NwAppnEventFilterTable_Object=MibTable
nwAppnEventFilterTable=_NwAppnEventFilterTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1))
if mibBuilder.loadTexts:nwAppnEventFilterTable.setStatus(_A)
_NwAppnEventFilterEntry_Object=MibTableRow
nwAppnEventFilterEntry=_NwAppnEventFilterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1))
nwAppnEventFilterEntry.setIndexNames((0,_G,_s),(0,_G,_t))
if mibBuilder.loadTexts:nwAppnEventFilterEntry.setStatus(_A)
_NwAppnEventFltrProtocol_Type=Integer32
_NwAppnEventFltrProtocol_Object=MibTableColumn
nwAppnEventFltrProtocol=_NwAppnEventFltrProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,1),_NwAppnEventFltrProtocol_Type())
nwAppnEventFltrProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventFltrProtocol.setStatus(_A)
_NwAppnEventFltrIfNum_Type=Integer32
_NwAppnEventFltrIfNum_Object=MibTableColumn
nwAppnEventFltrIfNum=_NwAppnEventFltrIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,2),_NwAppnEventFltrIfNum_Type())
nwAppnEventFltrIfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventFltrIfNum.setStatus(_A)
class _NwAppnEventFltrControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),('add',3)))
_NwAppnEventFltrControl_Type.__name__=_C
_NwAppnEventFltrControl_Object=MibTableColumn
nwAppnEventFltrControl=_NwAppnEventFltrControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,3),_NwAppnEventFltrControl_Type())
nwAppnEventFltrControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventFltrControl.setStatus(_A)
class _NwAppnEventFltrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwAppnEventFltrType_Type.__name__=_C
_NwAppnEventFltrType_Object=MibTableColumn
nwAppnEventFltrType=_NwAppnEventFltrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,4),_NwAppnEventFltrType_Type())
nwAppnEventFltrType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventFltrType.setStatus(_A)
class _NwAppnEventFltrSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_v,2),(_w,3)))
_NwAppnEventFltrSeverity_Type.__name__=_C
_NwAppnEventFltrSeverity_Object=MibTableColumn
nwAppnEventFltrSeverity=_NwAppnEventFltrSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,5),_NwAppnEventFltrSeverity_Type())
nwAppnEventFltrSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventFltrSeverity.setStatus(_A)
class _NwAppnEventFltrAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('logTrap',3)))
_NwAppnEventFltrAction_Type.__name__=_C
_NwAppnEventFltrAction_Object=MibTableColumn
nwAppnEventFltrAction=_NwAppnEventFltrAction_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,2,1,1,6),_NwAppnEventFltrAction_Type())
nwAppnEventFltrAction.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAppnEventFltrAction.setStatus(_A)
_NwAppnEventLogTable_ObjectIdentity=ObjectIdentity
nwAppnEventLogTable=_NwAppnEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3))
_NwAppnEventTable_Object=MibTable
nwAppnEventTable=_NwAppnEventTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1))
if mibBuilder.loadTexts:nwAppnEventTable.setStatus(_A)
_NwAppnEventEntry_Object=MibTableRow
nwAppnEventEntry=_NwAppnEventEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1))
nwAppnEventEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:nwAppnEventEntry.setStatus(_A)
_NwAppnEventNumber_Type=Integer32
_NwAppnEventNumber_Object=MibTableColumn
nwAppnEventNumber=_NwAppnEventNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,1),_NwAppnEventNumber_Type())
nwAppnEventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventNumber.setStatus(_A)
_NwAppnEventTime_Type=TimeTicks
_NwAppnEventTime_Object=MibTableColumn
nwAppnEventTime=_NwAppnEventTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,2),_NwAppnEventTime_Type())
nwAppnEventTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventTime.setStatus(_A)
class _NwAppnEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('diags',32),('error',64)))
_NwAppnEventType_Type.__name__=_C
_NwAppnEventType_Object=MibTableColumn
nwAppnEventType=_NwAppnEventType_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,3),_NwAppnEventType_Type())
nwAppnEventType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventType.setStatus(_A)
class _NwAppnEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_v,2),(_w,3)))
_NwAppnEventSeverity_Type.__name__=_C
_NwAppnEventSeverity_Object=MibTableColumn
nwAppnEventSeverity=_NwAppnEventSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,4),_NwAppnEventSeverity_Type())
nwAppnEventSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventSeverity.setStatus(_A)
_NwAppnEventProtocol_Type=Integer32
_NwAppnEventProtocol_Object=MibTableColumn
nwAppnEventProtocol=_NwAppnEventProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,5),_NwAppnEventProtocol_Type())
nwAppnEventProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventProtocol.setStatus(_A)
_NwAppnEventIfNum_Type=Integer32
_NwAppnEventIfNum_Object=MibTableColumn
nwAppnEventIfNum=_NwAppnEventIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,6),_NwAppnEventIfNum_Type())
nwAppnEventIfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventIfNum.setStatus(_A)
_NwAppnEventTextString_Type=OctetString
_NwAppnEventTextString_Object=MibTableColumn
nwAppnEventTextString=_NwAppnEventTextString_Object((1,3,6,1,4,1,52,4,2,2,2,3,5,2,10,3,1,1,7),_NwAppnEventTextString_Type())
nwAppnEventTextString.setMaxAccess(_D)
if mibBuilder.loadTexts:nwAppnEventTextString.setStatus(_A)
_NwAppnWorkGroup_ObjectIdentity=ObjectIdentity
nwAppnWorkGroup=_NwAppnWorkGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,5,2,11))
mibBuilder.exportSymbols(_G,**{'nwAppnRouter':nwAppnRouter,'nwAppnMibs':nwAppnMibs,'nwAppnMibRevText':nwAppnMibRevText,'nwAppnComponents':nwAppnComponents,'nwAppnSystem':nwAppnSystem,'nwAppnSysConfig':nwAppnSysConfig,'nwAppnSysRouterId':nwAppnSysRouterId,'nwAppnSysCfgLocalNode':nwAppnSysCfgLocalNode,'nwAppnSysNodeType':nwAppnSysNodeType,'nwAppnSysCpAlias':nwAppnSysCpAlias,'nwAppnSysModeCosMap':nwAppnSysModeCosMap,'nwAppnSysMdsSupport':nwAppnSysMdsSupport,'nwAppnSysMaxLocates':nwAppnSysMaxLocates,'nwAppnSysDirCacheSize':nwAppnSysDirCacheSize,'nwAppnSysMaxDirEntries':nwAppnSysMaxDirEntries,'nwAppnSysLocateTimeout':nwAppnSysLocateTimeout,'nwAppnSysRegCds':nwAppnSysRegCds,'nwAppnSysMdsSendQSize':nwAppnSysMdsSendQSize,'nwAppnSysCosSize':nwAppnSysCosSize,'nwAppnSysTreeSize':nwAppnSysTreeSize,'nwAppnSysTreeUseLimit':nwAppnSysTreeUseLimit,'nwAppnSysMaxTdmNodes':nwAppnSysMaxTdmNodes,'nwAppnSysMaxTdmTGs':nwAppnSysMaxTdmTGs,'nwAppnSysMaxIsrSessions':nwAppnSysMaxIsrSessions,'nwAppnSysIsrUpperThresh':nwAppnSysIsrUpperThresh,'nwAppnSysIsrLowerThresh':nwAppnSysIsrLowerThresh,'nwAppnSysIsrMaxRuSize':nwAppnSysIsrMaxRuSize,'nwAppnSysIsrRcvPaceWind':nwAppnSysIsrRcvPaceWind,'nwAppnSysRtAddResist':nwAppnSysRtAddResist,'nwAppnSysStopType':nwAppnSysStopType,'nwAppnSysBlockNum':nwAppnSysBlockNum,'nwAppnSysIdNum':nwAppnSysIdNum,'nwAppnSysCfgTables':nwAppnSysCfgTables,'nwAppnSysLuTable':nwAppnSysLuTable,'nwAppnSysLuEntry':nwAppnSysLuEntry,_h:nwAppnSysCpName,_i:nwAppnSysLuName,'nwAppnSysLuControl':nwAppnSysLuControl,'nwAppnSysAdministration':nwAppnSysAdministration,'nwAppnSysAdminStatus':nwAppnSysAdminStatus,'nwAppnSysOperStatus':nwAppnSysOperStatus,'nwAppnSysAdminReset':nwAppnSysAdminReset,'nwAppnSysOperationalTime':nwAppnSysOperationalTime,'nwAppnSysVersion':nwAppnSysVersion,'nwAppnForwarding':nwAppnForwarding,'nwAppnFwdSystem':nwAppnFwdSystem,'nwAppnFwdCounters':nwAppnFwdCounters,'nwAppnFwdCtrAdminStatus':nwAppnFwdCtrAdminStatus,'nwAppnFwdCtrReset':nwAppnFwdCtrReset,'nwAppnFwdCtrOperationalTime':nwAppnFwdCtrOperationalTime,'nwAppnFwdCtrInMus':nwAppnFwdCtrInMus,'nwAppnFwdCtrOutMus':nwAppnFwdCtrOutMus,'nwAppnFwdCtrFwdMus':nwAppnFwdCtrFwdMus,'nwAppnFwdCtrFilteredMus':nwAppnFwdCtrFilteredMus,'nwAppnFwdCtrDiscardMus':nwAppnFwdCtrDiscardMus,'nwAppnFwdCtrAddrErrMus':nwAppnFwdCtrAddrErrMus,'nwAppnFwdCtrLenErrMus':nwAppnFwdCtrLenErrMus,'nwAppnFwdCtrHdrErrMus':nwAppnFwdCtrHdrErrMus,'nwAppnFwdCtrInBytes':nwAppnFwdCtrInBytes,'nwAppnFwdCtrOutBytes':nwAppnFwdCtrOutBytes,'nwAppnFwdCtrFwdBytes':nwAppnFwdCtrFwdBytes,'nwAppnFwdCtrFilteredBytes':nwAppnFwdCtrFilteredBytes,'nwAppnFwdCtrDiscardBytes':nwAppnFwdCtrDiscardBytes,'nwAppnFwdCtrHostInMus':nwAppnFwdCtrHostInMus,'nwAppnFwdCtrHostOutMus':nwAppnFwdCtrHostOutMus,'nwAppnFwdCtrHostDiscardMus':nwAppnFwdCtrHostDiscardMus,'nwAppnFwdCtrHostInBytes':nwAppnFwdCtrHostInBytes,'nwAppnFwdCtrHostOutBytes':nwAppnFwdCtrHostOutBytes,'nwAppnFwdCtrHostDiscardBytes':nwAppnFwdCtrHostDiscardBytes,'nwAppnFwdInterfaces':nwAppnFwdInterfaces,'nwAppnFwdIfConfig':nwAppnFwdIfConfig,'nwAppnFwdIfTable':nwAppnFwdIfTable,'nwAppnFwdIfEntry':nwAppnFwdIfEntry,_j:nwAppnFwdIfIndex,'nwAppnFwdIfAdminStatus':nwAppnFwdIfAdminStatus,'nwAppnFwdIfOperStatus':nwAppnFwdIfOperStatus,'nwAppnFwdIfOperationalTime':nwAppnFwdIfOperationalTime,'nwAppnFwdIfControl':nwAppnFwdIfControl,'nwAppnFwdIfMtu':nwAppnFwdIfMtu,'nwAppnFwdIfForwarding':nwAppnFwdIfForwarding,'nwAppnFwdIfFrameType':nwAppnFwdIfFrameType,'nwAppnFwdIfAclIdentifier':nwAppnFwdIfAclIdentifier,'nwAppnFwdIfAclStatus':nwAppnFwdIfAclStatus,'nwAppnFwdIfCacheControl':nwAppnFwdIfCacheControl,'nwAppnFwdIfCacheEntries':nwAppnFwdIfCacheEntries,'nwAppnFwdIfCacheHits':nwAppnFwdIfCacheHits,'nwAppnFwdIfCacheMisses':nwAppnFwdIfCacheMisses,'nwAppnExtensionTable':nwAppnExtensionTable,'nwAppnExtEntry':nwAppnExtEntry,_k:nwAppnExtIfIndex,'nwAppnExtIfPortName':nwAppnExtIfPortName,'nwAppnExtIfPortType':nwAppnExtIfPortType,'nwAppnExtIfDlcType':nwAppnExtIfDlcType,'nwAppnExtIfMaxRBtuSize':nwAppnExtIfMaxRBtuSize,'nwAppnExtIfTotLsActLim':nwAppnExtIfTotLsActLim,'nwAppnExtIfInbLsActLim':nwAppnExtIfInbLsActLim,'nwAppnExtIfOutbLsActLim':nwAppnExtIfOutbLsActLim,'nwAppnExtIfLocalLsRole':nwAppnExtIfLocalLsRole,'nwAppnExtIfActXidXchgLimit':nwAppnExtIfActXidXchgLimit,'nwAppnExtIfNonActXidXchgLimit':nwAppnExtIfNonActXidXchgLimit,'nwAppnExtIfLsXmitRcvCap':nwAppnExtIfLsXmitRcvCap,'nwAppnExtIfMaxIfrmRcvd':nwAppnExtIfMaxIfrmRcvd,'nwAppnExtIfDfltTargetPacing':nwAppnExtIfDfltTargetPacing,'nwAppnExtIfDfltMaxSBtuSize':nwAppnExtIfDfltMaxSBtuSize,'nwAppnExtIfDfltEffectCap':nwAppnExtIfDfltEffectCap,'nwAppnExtIfDfltConnectCost':nwAppnExtIfDfltConnectCost,'nwAppnExtIfDfltByteCost':nwAppnExtIfDfltByteCost,'nwAppnExtIfDfltSecurity':nwAppnExtIfDfltSecurity,'nwAppnExtIfDfltPropDelay':nwAppnExtIfDfltPropDelay,'nwAppnExtIfDfltUsrDef1':nwAppnExtIfDfltUsrDef1,'nwAppnExtIfDfltUsrDef2':nwAppnExtIfDfltUsrDef2,'nwAppnExtIfDfltUsrDef3':nwAppnExtIfDfltUsrDef3,'nwAppnExtIfStopType':nwAppnExtIfStopType,'nwAppnExtIfCpCpSupp':nwAppnExtIfCpCpSupp,'nwAppnExtIfLimitedRsrc':nwAppnExtIfLimitedRsrc,'nwAppnExtIfAddress':nwAppnExtIfAddress,'nwAppnExtIfSsap':nwAppnExtIfSsap,'nwAppnIfCn':nwAppnIfCn,'nwAppnIfCnPortTable':nwAppnIfCnPortTable,'nwAppnIfCnPortEntry':nwAppnIfCnPortEntry,_m:nwAppnIfCnPtFqName,_n:nwAppnIfCnPtName,'nwAppnIfCnPtControl':nwAppnIfCnPtControl,'nwAppnIfCnTgCharTable':nwAppnIfCnTgCharTable,'nwAppnIfCnTgCharEntry':nwAppnIfCnTgCharEntry,_o:nwAppnIfCnTgFqName,'nwAppnIfCnTgEffectCap':nwAppnIfCnTgEffectCap,'nwAppnIfCnTgConnectCost':nwAppnIfCnTgConnectCost,'nwAppnIfCnTgByteCost':nwAppnIfCnTgByteCost,'nwAppnIfCnTgSecurity':nwAppnIfCnTgSecurity,'nwAppnIfCnTgPropDelay':nwAppnIfCnTgPropDelay,'nwAppnIfCnTgUsrDef1':nwAppnIfCnTgUsrDef1,'nwAppnIfCnTgUsrDef2':nwAppnIfCnTgUsrDef2,'nwAppnIfCnTgUsrDef3':nwAppnIfCnTgUsrDef3,'nwAppnFwdIfCounters':nwAppnFwdIfCounters,'nwAppnFwdIfCtrTable':nwAppnFwdIfCtrTable,'nwAppnFwdIfCtrEntry':nwAppnFwdIfCtrEntry,_p:nwAppnFwdIfCtrIfIndex,'nwAppnFwdIfCtrAdminStatus':nwAppnFwdIfCtrAdminStatus,'nwAppnFwdIfCtrReset':nwAppnFwdIfCtrReset,'nwAppnFwdIfCtrOperationalTime':nwAppnFwdIfCtrOperationalTime,'nwAppnFwdIfCtrInMus':nwAppnFwdIfCtrInMus,'nwAppnFwdIfCtrOutMus':nwAppnFwdIfCtrOutMus,'nwAppnFwdIfCtrFwdMus':nwAppnFwdIfCtrFwdMus,'nwAppnFwdIfCtrFilteredMus':nwAppnFwdIfCtrFilteredMus,'nwAppnFwdIfCtrDiscardMus':nwAppnFwdIfCtrDiscardMus,'nwAppnFwdIfCtrAddrErrMus':nwAppnFwdIfCtrAddrErrMus,'nwAppnFwdIfCtrLenErrMus':nwAppnFwdIfCtrLenErrMus,'nwAppnFwdIfCtrHdrErrMus':nwAppnFwdIfCtrHdrErrMus,'nwAppnFwdIfCtrInBytes':nwAppnFwdIfCtrInBytes,'nwAppnFwdIfCtrOutBytes':nwAppnFwdIfCtrOutBytes,'nwAppnFwdIfCtrFwdBytes':nwAppnFwdIfCtrFwdBytes,'nwAppnFwdIfCtrFilteredBytes':nwAppnFwdIfCtrFilteredBytes,'nwAppnFwdIfCtrDiscardBytes':nwAppnFwdIfCtrDiscardBytes,'nwAppnFwdIfCtrHostInMus':nwAppnFwdIfCtrHostInMus,'nwAppnFwdIfCtrHostOutMus':nwAppnFwdIfCtrHostOutMus,'nwAppnFwdIfCtrHostDiscardMus':nwAppnFwdIfCtrHostDiscardMus,'nwAppnFwdIfCtrHostInBytes':nwAppnFwdIfCtrHostInBytes,'nwAppnFwdIfCtrHostOutBytes':nwAppnFwdIfCtrHostOutBytes,'nwAppnFwdIfCtrHostDiscardBytes':nwAppnFwdIfCtrHostDiscardBytes,'nwAppnFwdLinks':nwAppnFwdLinks,'nwAppnFwdLsConfig':nwAppnFwdLsConfig,'nwAppnFwdLsTable':nwAppnFwdLsTable,'nwAppnFwdLsEntry':nwAppnFwdLsEntry,_q:nwAppnFwdLsName,'nwAppnFwdLsAdminStatus':nwAppnFwdLsAdminStatus,'nwAppnFwdLsOperStatus':nwAppnFwdLsOperStatus,'nwAppnFwdLsOperationalTime':nwAppnFwdLsOperationalTime,'nwAppnFwdLsControl':nwAppnFwdLsControl,'nwAppnFwdLsPortName':nwAppnFwdLsPortName,'nwAppnFwdLsAdjCpName':nwAppnFwdLsAdjCpName,'nwAppnFwdLsAdjCpType':nwAppnFwdLsAdjCpType,'nwAppnFwdLsAutoActSupport':nwAppnFwdLsAutoActSupport,'nwAppnFwdLsLimitedRsrc':nwAppnFwdLsLimitedRsrc,'nwAppnFwdLsSscpSession':nwAppnFwdLsSscpSession,'nwAppnFwdLsPuName':nwAppnFwdLsPuName,'nwAppnFwdLsBackLvlLenEN':nwAppnFwdLsBackLvlLenEN,'nwAppnFwdLsCpCpSessSupp':nwAppnFwdLsCpCpSessSupp,'nwAppnFwdLsEffectCap':nwAppnFwdLsEffectCap,'nwAppnFwdLsConnectCost':nwAppnFwdLsConnectCost,'nwAppnFwdLsByteCost':nwAppnFwdLsByteCost,'nwAppnFwdLsSecurity':nwAppnFwdLsSecurity,'nwAppnFwdLsPropDelay':nwAppnFwdLsPropDelay,'nwAppnFwdLsUsrDef1':nwAppnFwdLsUsrDef1,'nwAppnFwdLsUsrDef2':nwAppnFwdLsUsrDef2,'nwAppnFwdLsUsrDef3':nwAppnFwdLsUsrDef3,'nwAppnFwdLsTrgtPacingCount':nwAppnFwdLsTrgtPacingCount,'nwAppnFwdLsMaxSendBtu':nwAppnFwdLsMaxSendBtu,'nwAppnFwdLsNumActiveSession':nwAppnFwdLsNumActiveSession,'nwAppnFwdLsdynamicLs':nwAppnFwdLsdynamicLs,'nwAppnFwdLsStopType':nwAppnFwdLsStopType,'nwAppnFwdLsPortNbr':nwAppnFwdLsPortNbr,'nwAppnFwdLsDestAddr':nwAppnFwdLsDestAddr,'nwAppnFwdLsDsap':nwAppnFwdLsDsap,'nwAppnFwdLsBlockNum':nwAppnFwdLsBlockNum,'nwAppnFwdLsIdNum':nwAppnFwdLsIdNum,'nwAppnFwdLsCounters':nwAppnFwdLsCounters,'nwAppnFwdLsCtrTable':nwAppnFwdLsCtrTable,'nwAppnFwdLsCtrEntry':nwAppnFwdLsCtrEntry,_r:nwAppnFwdLsCtrLsName,'nwAppnFwdLsCtrAdminStatus':nwAppnFwdLsCtrAdminStatus,'nwAppnFwdLsCtrReset':nwAppnFwdLsCtrReset,'nwAppnFwdLsCtrOperationalTime':nwAppnFwdLsCtrOperationalTime,'nwAppnFwdLsCtrInBlus':nwAppnFwdLsCtrInBlus,'nwAppnFwdLsCtrOutBlus':nwAppnFwdLsCtrOutBlus,'nwAppnFwdLsCtrFwdBlus':nwAppnFwdLsCtrFwdBlus,'nwAppnFwdLsCtrFilteredBlus':nwAppnFwdLsCtrFilteredBlus,'nwAppnFwdLsCtrDiscardBlus':nwAppnFwdLsCtrDiscardBlus,'nwAppnFwdLsCtrAddrErrBlus':nwAppnFwdLsCtrAddrErrBlus,'nwAppnFwdLsCtrLenErrBlus':nwAppnFwdLsCtrLenErrBlus,'nwAppnFwdLsCtrHdrErrBlus':nwAppnFwdLsCtrHdrErrBlus,'nwAppnFwdLsCtrInBytes':nwAppnFwdLsCtrInBytes,'nwAppnFwdLsCtrOutBytes':nwAppnFwdLsCtrOutBytes,'nwAppnFwdLsCtrFwdBytes':nwAppnFwdLsCtrFwdBytes,'nwAppnFwdLsCtrFilteredBytes':nwAppnFwdLsCtrFilteredBytes,'nwAppnFwdLsCtrDiscardBytes':nwAppnFwdLsCtrDiscardBytes,'nwAppnFwdLsCtrHostInBlus':nwAppnFwdLsCtrHostInBlus,'nwAppnFwdLsCtrHostOutBlus':nwAppnFwdLsCtrHostOutBlus,'nwAppnFwdLsCtrHostDiscardBlus':nwAppnFwdLsCtrHostDiscardBlus,'nwAppnFwdLsCtrHostInBytes':nwAppnFwdLsCtrHostInBytes,'nwAppnFwdLsCtrHostOutBytes':nwAppnFwdLsCtrHostOutBytes,'nwAppnFwdLsCtrHostDiscardBytes':nwAppnFwdLsCtrHostDiscardBytes,'nwAppnTopology':nwAppnTopology,'nwAppnDistanceVector':nwAppnDistanceVector,'nwAppnLinkState':nwAppnLinkState,'nwAppnIsr':nwAppnIsr,'nwAppnIsrSystem':nwAppnIsrSystem,'nwAppnIsrConfig':nwAppnIsrConfig,'nwAppnIsrAdminStatus':nwAppnIsrAdminStatus,'nwAppnIsrOperStatus':nwAppnIsrOperStatus,'nwAppnIsrAdminReset':nwAppnIsrAdminReset,'nwAppnIsrOperationalTime':nwAppnIsrOperationalTime,'nwAppnIsrVersion':nwAppnIsrVersion,'nwAppnIsrCounters':nwAppnIsrCounters,'nwAppnIsrInterfaces':nwAppnIsrInterfaces,'nwAppnIsrIfConfig':nwAppnIsrIfConfig,'nwAppnIsrIfCounters':nwAppnIsrIfCounters,'nwAppnIsrDatabase':nwAppnIsrDatabase,'nwAppnIsrFilters':nwAppnIsrFilters,'nwAppnFib':nwAppnFib,'nwAppnEndSystems':nwAppnEndSystems,'nwAppnHostsSystem':nwAppnHostsSystem,'nwAppnHostsInterfaces':nwAppnHostsInterfaces,'nwAppnAccessControl':nwAppnAccessControl,'nwAppnFilters':nwAppnFilters,'nwAppnRedirector':nwAppnRedirector,'nwAppnEvent':nwAppnEvent,'nwAppnEventLogConfig':nwAppnEventLogConfig,'nwAppnEventAdminStatus':nwAppnEventAdminStatus,'nwAppnEventMaxEntries':nwAppnEventMaxEntries,'nwAppnEventTraceAll':nwAppnEventTraceAll,'nwAppnEventLogFilterTable':nwAppnEventLogFilterTable,'nwAppnEventFilterTable':nwAppnEventFilterTable,'nwAppnEventFilterEntry':nwAppnEventFilterEntry,_s:nwAppnEventFltrProtocol,_t:nwAppnEventFltrIfNum,'nwAppnEventFltrControl':nwAppnEventFltrControl,'nwAppnEventFltrType':nwAppnEventFltrType,'nwAppnEventFltrSeverity':nwAppnEventFltrSeverity,'nwAppnEventFltrAction':nwAppnEventFltrAction,'nwAppnEventLogTable':nwAppnEventLogTable,'nwAppnEventTable':nwAppnEventTable,'nwAppnEventEntry':nwAppnEventEntry,_x:nwAppnEventNumber,'nwAppnEventTime':nwAppnEventTime,'nwAppnEventType':nwAppnEventType,'nwAppnEventSeverity':nwAppnEventSeverity,'nwAppnEventProtocol':nwAppnEventProtocol,'nwAppnEventIfNum':nwAppnEventIfNum,'nwAppnEventTextString':nwAppnEventTextString,'nwAppnWorkGroup':nwAppnWorkGroup})