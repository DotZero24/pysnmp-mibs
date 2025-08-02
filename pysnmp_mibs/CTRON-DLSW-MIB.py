_g='ctdlswEventNumber'
_f='highlow'
_e='highmed'
_d='highest'
_c='ctdlswEventFltrIfNum'
_b='ctdlswEventFltrProtocol'
_a='ctdlswTConnRemoteTAddr'
_Z='ctdlswRemoteMacFilterDestMask'
_Y='ctdlswRemoteMacFilterDestAddr'
_X='ctdlswRemoteMacFilterSrcMask'
_W='ctdlswRemoteMacFilterSrcAddr'
_V='ctdlswLocalMacFilterDestMask'
_U='ctdlswLocalMacFilterDestAddr'
_T='ctdlswLocalMacFilterSrcMask'
_S='ctdlswLocalMacFilterSrcAddr'
_R='ctdlswRemoteNBFilterDestName'
_Q='ctdlswRemoteNBFilterSrcName'
_P='ctdlswLocalNBFilterDestName'
_O='ctdlswLocalNBFilterSrcName'
_N='ctdlswPortName'
_M='DisplayString'
_L='pass'
_K='block'
_J='create'
_I='delete'
_H='enabled'
_G='disabled'
_F='other'
_E='CTRON-DLSW-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
ctDLSW,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDLSW')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
class NBName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtdlswNode_ObjectIdentity=ObjectIdentity
ctdlswNode=_CtdlswNode_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,1))
_CtdlswNodeConfig_ObjectIdentity=ObjectIdentity
ctdlswNodeConfig=_CtdlswNodeConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,1,1))
_CtdlswVersion_Type=DisplayString
_CtdlswVersion_Object=MibScalar
ctdlswVersion=_CtdlswVersion_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,1),_CtdlswVersion_Type())
ctdlswVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswVersion.setStatus(_A)
class _CtdlswAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('disable',2),('enable',3)))
_CtdlswAdminStatus_Type.__name__=_C
_CtdlswAdminStatus_Object=MibScalar
ctdlswAdminStatus=_CtdlswAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,2),_CtdlswAdminStatus_Type())
ctdlswAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswAdminStatus.setStatus(_A)
class _CtdlswOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtdlswOperStatus_Type.__name__=_C
_CtdlswOperStatus_Object=MibScalar
ctdlswOperStatus=_CtdlswOperStatus_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,3),_CtdlswOperStatus_Type())
ctdlswOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswOperStatus.setStatus(_A)
_CtdlswUpTime_Type=TimeTicks
_CtdlswUpTime_Object=MibScalar
ctdlswUpTime=_CtdlswUpTime_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,4),_CtdlswUpTime_Type())
ctdlswUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswUpTime.setStatus(_A)
class _CtdlswOperVirtualRingNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CtdlswOperVirtualRingNumber_Type.__name__=_C
_CtdlswOperVirtualRingNumber_Object=MibScalar
ctdlswOperVirtualRingNumber=_CtdlswOperVirtualRingNumber_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,5),_CtdlswOperVirtualRingNumber_Type())
ctdlswOperVirtualRingNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswOperVirtualRingNumber.setStatus(_A)
class _CtdlswNBLocalFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CtdlswNBLocalFilterType_Type.__name__=_C
_CtdlswNBLocalFilterType_Object=MibScalar
ctdlswNBLocalFilterType=_CtdlswNBLocalFilterType_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,6),_CtdlswNBLocalFilterType_Type())
ctdlswNBLocalFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswNBLocalFilterType.setStatus(_A)
class _CtdlswNBRemoteFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CtdlswNBRemoteFilterType_Type.__name__=_C
_CtdlswNBRemoteFilterType_Object=MibScalar
ctdlswNBRemoteFilterType=_CtdlswNBRemoteFilterType_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,7),_CtdlswNBRemoteFilterType_Type())
ctdlswNBRemoteFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswNBRemoteFilterType.setStatus(_A)
class _CtdlswMacLocalFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CtdlswMacLocalFilterType_Type.__name__=_C
_CtdlswMacLocalFilterType_Object=MibScalar
ctdlswMacLocalFilterType=_CtdlswMacLocalFilterType_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,8),_CtdlswMacLocalFilterType_Type())
ctdlswMacLocalFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswMacLocalFilterType.setStatus(_A)
class _CtdlswMacRemoteFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CtdlswMacRemoteFilterType_Type.__name__=_C
_CtdlswMacRemoteFilterType_Object=MibScalar
ctdlswMacRemoteFilterType=_CtdlswMacRemoteFilterType_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,9),_CtdlswMacRemoteFilterType_Type())
ctdlswMacRemoteFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswMacRemoteFilterType.setStatus(_A)
class _CtdlswAcceptDynamicTConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_CtdlswAcceptDynamicTConn_Type.__name__=_C
_CtdlswAcceptDynamicTConn_Object=MibScalar
ctdlswAcceptDynamicTConn=_CtdlswAcceptDynamicTConn_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,10),_CtdlswAcceptDynamicTConn_Type())
ctdlswAcceptDynamicTConn.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswAcceptDynamicTConn.setStatus(_A)
_CtdlswDefaultPortNumber_Type=Integer32
_CtdlswDefaultPortNumber_Object=MibScalar
ctdlswDefaultPortNumber=_CtdlswDefaultPortNumber_Object((1,3,6,1,4,1,52,4,1,2,8,1,1,11),_CtdlswDefaultPortNumber_Type())
ctdlswDefaultPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswDefaultPortNumber.setStatus(_A)
_CtdlswPort_ObjectIdentity=ObjectIdentity
ctdlswPort=_CtdlswPort_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,2))
_CtdlswPortTable_Object=MibTable
ctdlswPortTable=_CtdlswPortTable_Object((1,3,6,1,4,1,52,4,1,2,8,2,1))
if mibBuilder.loadTexts:ctdlswPortTable.setStatus(_A)
_CtdlswPortEntry_Object=MibTableRow
ctdlswPortEntry=_CtdlswPortEntry_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1))
ctdlswPortEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:ctdlswPortEntry.setStatus(_A)
_CtdlswPortIndex_Type=Integer32
_CtdlswPortIndex_Object=MibTableColumn
ctdlswPortIndex=_CtdlswPortIndex_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,1),_CtdlswPortIndex_Type())
ctdlswPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswPortIndex.setStatus(_A)
class _CtdlswPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_CtdlswPortName_Type.__name__=_M
_CtdlswPortName_Object=MibTableColumn
ctdlswPortName=_CtdlswPortName_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,2),_CtdlswPortName_Type())
ctdlswPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswPortName.setStatus(_A)
_CtdlswPortAddress_Type=MacAddress
_CtdlswPortAddress_Object=MibTableColumn
ctdlswPortAddress=_CtdlswPortAddress_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,3),_CtdlswPortAddress_Type())
ctdlswPortAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswPortAddress.setStatus(_A)
class _CtdlswPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtdlswPortAdminStatus_Type.__name__=_C
_CtdlswPortAdminStatus_Object=MibTableColumn
ctdlswPortAdminStatus=_CtdlswPortAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,4),_CtdlswPortAdminStatus_Type())
ctdlswPortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswPortAdminStatus.setStatus(_A)
class _CtdlswPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtdlswPortOperStatus_Type.__name__=_C
_CtdlswPortOperStatus_Object=MibTableColumn
ctdlswPortOperStatus=_CtdlswPortOperStatus_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,5),_CtdlswPortOperStatus_Type())
ctdlswPortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswPortOperStatus.setStatus(_A)
_CtdlswPortUpTime_Type=TimeTicks
_CtdlswPortUpTime_Object=MibTableColumn
ctdlswPortUpTime=_CtdlswPortUpTime_Object((1,3,6,1,4,1,52,4,1,2,8,2,1,1,6),_CtdlswPortUpTime_Type())
ctdlswPortUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswPortUpTime.setStatus(_A)
_CtdlswFilter_ObjectIdentity=ObjectIdentity
ctdlswFilter=_CtdlswFilter_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,3))
_CtdlswLocalNBFilterTable_Object=MibTable
ctdlswLocalNBFilterTable=_CtdlswLocalNBFilterTable_Object((1,3,6,1,4,1,52,4,1,2,8,3,1))
if mibBuilder.loadTexts:ctdlswLocalNBFilterTable.setStatus(_A)
_CtdlswLocalNBFilterEntry_Object=MibTableRow
ctdlswLocalNBFilterEntry=_CtdlswLocalNBFilterEntry_Object((1,3,6,1,4,1,52,4,1,2,8,3,1,1))
ctdlswLocalNBFilterEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:ctdlswLocalNBFilterEntry.setStatus(_A)
_CtdlswLocalNBFilterSrcName_Type=NBName
_CtdlswLocalNBFilterSrcName_Object=MibTableColumn
ctdlswLocalNBFilterSrcName=_CtdlswLocalNBFilterSrcName_Object((1,3,6,1,4,1,52,4,1,2,8,3,1,1,1),_CtdlswLocalNBFilterSrcName_Type())
ctdlswLocalNBFilterSrcName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalNBFilterSrcName.setStatus(_A)
_CtdlswLocalNBFilterDestName_Type=NBName
_CtdlswLocalNBFilterDestName_Object=MibTableColumn
ctdlswLocalNBFilterDestName=_CtdlswLocalNBFilterDestName_Object((1,3,6,1,4,1,52,4,1,2,8,3,1,1,2),_CtdlswLocalNBFilterDestName_Type())
ctdlswLocalNBFilterDestName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalNBFilterDestName.setStatus(_A)
class _CtdlswLocalNBFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_J,2),(_I,3)))
_CtdlswLocalNBFilterControl_Type.__name__=_C
_CtdlswLocalNBFilterControl_Object=MibTableColumn
ctdlswLocalNBFilterControl=_CtdlswLocalNBFilterControl_Object((1,3,6,1,4,1,52,4,1,2,8,3,1,1,3),_CtdlswLocalNBFilterControl_Type())
ctdlswLocalNBFilterControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswLocalNBFilterControl.setStatus(_A)
_CtdlswRemoteNBFilterTable_Object=MibTable
ctdlswRemoteNBFilterTable=_CtdlswRemoteNBFilterTable_Object((1,3,6,1,4,1,52,4,1,2,8,3,2))
if mibBuilder.loadTexts:ctdlswRemoteNBFilterTable.setStatus(_A)
_CtdlswRemoteNBFilterEntry_Object=MibTableRow
ctdlswRemoteNBFilterEntry=_CtdlswRemoteNBFilterEntry_Object((1,3,6,1,4,1,52,4,1,2,8,3,2,1))
ctdlswRemoteNBFilterEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:ctdlswRemoteNBFilterEntry.setStatus(_A)
_CtdlswRemoteNBFilterSrcName_Type=NBName
_CtdlswRemoteNBFilterSrcName_Object=MibTableColumn
ctdlswRemoteNBFilterSrcName=_CtdlswRemoteNBFilterSrcName_Object((1,3,6,1,4,1,52,4,1,2,8,3,2,1,1),_CtdlswRemoteNBFilterSrcName_Type())
ctdlswRemoteNBFilterSrcName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteNBFilterSrcName.setStatus(_A)
_CtdlswRemoteNBFilterDestName_Type=NBName
_CtdlswRemoteNBFilterDestName_Object=MibTableColumn
ctdlswRemoteNBFilterDestName=_CtdlswRemoteNBFilterDestName_Object((1,3,6,1,4,1,52,4,1,2,8,3,2,1,2),_CtdlswRemoteNBFilterDestName_Type())
ctdlswRemoteNBFilterDestName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteNBFilterDestName.setStatus(_A)
class _CtdlswRemoteNBFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_J,2),(_I,3)))
_CtdlswRemoteNBFilterControl_Type.__name__=_C
_CtdlswRemoteNBFilterControl_Object=MibTableColumn
ctdlswRemoteNBFilterControl=_CtdlswRemoteNBFilterControl_Object((1,3,6,1,4,1,52,4,1,2,8,3,2,1,3),_CtdlswRemoteNBFilterControl_Type())
ctdlswRemoteNBFilterControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswRemoteNBFilterControl.setStatus(_A)
_CtdlswLocalMacFilterTable_Object=MibTable
ctdlswLocalMacFilterTable=_CtdlswLocalMacFilterTable_Object((1,3,6,1,4,1,52,4,1,2,8,3,3))
if mibBuilder.loadTexts:ctdlswLocalMacFilterTable.setStatus(_A)
_CtdlswLocalMacFilterEntry_Object=MibTableRow
ctdlswLocalMacFilterEntry=_CtdlswLocalMacFilterEntry_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1))
ctdlswLocalMacFilterEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:ctdlswLocalMacFilterEntry.setStatus(_A)
_CtdlswLocalMacFilterSrcAddr_Type=MacAddress
_CtdlswLocalMacFilterSrcAddr_Object=MibTableColumn
ctdlswLocalMacFilterSrcAddr=_CtdlswLocalMacFilterSrcAddr_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1,1),_CtdlswLocalMacFilterSrcAddr_Type())
ctdlswLocalMacFilterSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalMacFilterSrcAddr.setStatus(_A)
_CtdlswLocalMacFilterSrcMask_Type=MacAddress
_CtdlswLocalMacFilterSrcMask_Object=MibTableColumn
ctdlswLocalMacFilterSrcMask=_CtdlswLocalMacFilterSrcMask_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1,2),_CtdlswLocalMacFilterSrcMask_Type())
ctdlswLocalMacFilterSrcMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalMacFilterSrcMask.setStatus(_A)
_CtdlswLocalMacFilterDestAddr_Type=MacAddress
_CtdlswLocalMacFilterDestAddr_Object=MibTableColumn
ctdlswLocalMacFilterDestAddr=_CtdlswLocalMacFilterDestAddr_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1,3),_CtdlswLocalMacFilterDestAddr_Type())
ctdlswLocalMacFilterDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalMacFilterDestAddr.setStatus(_A)
_CtdlswLocalMacFilterDestMask_Type=MacAddress
_CtdlswLocalMacFilterDestMask_Object=MibTableColumn
ctdlswLocalMacFilterDestMask=_CtdlswLocalMacFilterDestMask_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1,4),_CtdlswLocalMacFilterDestMask_Type())
ctdlswLocalMacFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswLocalMacFilterDestMask.setStatus(_A)
class _CtdlswLocalMacFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_J,2),(_I,3)))
_CtdlswLocalMacFilterControl_Type.__name__=_C
_CtdlswLocalMacFilterControl_Object=MibTableColumn
ctdlswLocalMacFilterControl=_CtdlswLocalMacFilterControl_Object((1,3,6,1,4,1,52,4,1,2,8,3,3,1,5),_CtdlswLocalMacFilterControl_Type())
ctdlswLocalMacFilterControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswLocalMacFilterControl.setStatus(_A)
_CtdlswRemoteMacFilterTable_Object=MibTable
ctdlswRemoteMacFilterTable=_CtdlswRemoteMacFilterTable_Object((1,3,6,1,4,1,52,4,1,2,8,3,4))
if mibBuilder.loadTexts:ctdlswRemoteMacFilterTable.setStatus(_A)
_CtdlswRemoteMacFilterEntry_Object=MibTableRow
ctdlswRemoteMacFilterEntry=_CtdlswRemoteMacFilterEntry_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1))
ctdlswRemoteMacFilterEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:ctdlswRemoteMacFilterEntry.setStatus(_A)
_CtdlswRemoteMacFilterSrcAddr_Type=MacAddress
_CtdlswRemoteMacFilterSrcAddr_Object=MibTableColumn
ctdlswRemoteMacFilterSrcAddr=_CtdlswRemoteMacFilterSrcAddr_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1,1),_CtdlswRemoteMacFilterSrcAddr_Type())
ctdlswRemoteMacFilterSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteMacFilterSrcAddr.setStatus(_A)
_CtdlswRemoteMacFilterSrcMask_Type=MacAddress
_CtdlswRemoteMacFilterSrcMask_Object=MibTableColumn
ctdlswRemoteMacFilterSrcMask=_CtdlswRemoteMacFilterSrcMask_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1,2),_CtdlswRemoteMacFilterSrcMask_Type())
ctdlswRemoteMacFilterSrcMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteMacFilterSrcMask.setStatus(_A)
_CtdlswRemoteMacFilterDestAddr_Type=MacAddress
_CtdlswRemoteMacFilterDestAddr_Object=MibTableColumn
ctdlswRemoteMacFilterDestAddr=_CtdlswRemoteMacFilterDestAddr_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1,3),_CtdlswRemoteMacFilterDestAddr_Type())
ctdlswRemoteMacFilterDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteMacFilterDestAddr.setStatus(_A)
_CtdlswRemoteMacFilterDestMask_Type=MacAddress
_CtdlswRemoteMacFilterDestMask_Object=MibTableColumn
ctdlswRemoteMacFilterDestMask=_CtdlswRemoteMacFilterDestMask_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1,4),_CtdlswRemoteMacFilterDestMask_Type())
ctdlswRemoteMacFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswRemoteMacFilterDestMask.setStatus(_A)
class _CtdlswRemoteMacFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_J,2),(_I,3)))
_CtdlswRemoteMacFilterControl_Type.__name__=_C
_CtdlswRemoteMacFilterControl_Object=MibTableColumn
ctdlswRemoteMacFilterControl=_CtdlswRemoteMacFilterControl_Object((1,3,6,1,4,1,52,4,1,2,8,3,4,1,5),_CtdlswRemoteMacFilterControl_Type())
ctdlswRemoteMacFilterControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswRemoteMacFilterControl.setStatus(_A)
_CtdlswTConn_ObjectIdentity=ObjectIdentity
ctdlswTConn=_CtdlswTConn_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,4))
_CtdlswTConnTable_Object=MibTable
ctdlswTConnTable=_CtdlswTConnTable_Object((1,3,6,1,4,1,52,4,1,2,8,4,1))
if mibBuilder.loadTexts:ctdlswTConnTable.setStatus(_A)
_CtdlswTConnEntry_Object=MibTableRow
ctdlswTConnEntry=_CtdlswTConnEntry_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1))
ctdlswTConnEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:ctdlswTConnEntry.setStatus(_A)
_CtdlswTConnRemoteTAddr_Type=IpAddress
_CtdlswTConnRemoteTAddr_Object=MibTableColumn
ctdlswTConnRemoteTAddr=_CtdlswTConnRemoteTAddr_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1,1),_CtdlswTConnRemoteTAddr_Type())
ctdlswTConnRemoteTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswTConnRemoteTAddr.setStatus(_A)
class _CtdlswTConnControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_J,2),(_I,3)))
_CtdlswTConnControl_Type.__name__=_C
_CtdlswTConnControl_Object=MibTableColumn
ctdlswTConnControl=_CtdlswTConnControl_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1,2),_CtdlswTConnControl_Type())
ctdlswTConnControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswTConnControl.setStatus(_A)
_CtdlswTConnUpTime_Type=TimeTicks
_CtdlswTConnUpTime_Object=MibTableColumn
ctdlswTConnUpTime=_CtdlswTConnUpTime_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1,3),_CtdlswTConnUpTime_Type())
ctdlswTConnUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswTConnUpTime.setStatus(_A)
class _CtdlswTConnOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),('pendingDisable',4),('pendingEnable',5)))
_CtdlswTConnOperStatus_Type.__name__=_C
_CtdlswTConnOperStatus_Object=MibTableColumn
ctdlswTConnOperStatus=_CtdlswTConnOperStatus_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1,4),_CtdlswTConnOperStatus_Type())
ctdlswTConnOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswTConnOperStatus.setStatus(_A)
class _CtdlswTConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configured',1),('dynamic',2)))
_CtdlswTConnType_Type.__name__=_C
_CtdlswTConnType_Object=MibTableColumn
ctdlswTConnType=_CtdlswTConnType_Object((1,3,6,1,4,1,52,4,1,2,8,4,1,1,5),_CtdlswTConnType_Type())
ctdlswTConnType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswTConnType.setStatus(_A)
_CtdlswTrap_ObjectIdentity=ObjectIdentity
ctdlswTrap=_CtdlswTrap_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,5))
_CtdlswEvent_ObjectIdentity=ObjectIdentity
ctdlswEvent=_CtdlswEvent_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,6))
_CtdlswEventLogConfig_ObjectIdentity=ObjectIdentity
ctdlswEventLogConfig=_CtdlswEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,6,1))
class _CtdlswEventAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtdlswEventAdminStatus_Type.__name__=_C
_CtdlswEventAdminStatus_Object=MibScalar
ctdlswEventAdminStatus=_CtdlswEventAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,8,6,1,1),_CtdlswEventAdminStatus_Type())
ctdlswEventAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventAdminStatus.setStatus(_A)
class _CtdlswEventMaxEntries_Type(Integer32):defaultValue=100
_CtdlswEventMaxEntries_Type.__name__=_C
_CtdlswEventMaxEntries_Object=MibScalar
ctdlswEventMaxEntries=_CtdlswEventMaxEntries_Object((1,3,6,1,4,1,52,4,1,2,8,6,1,2),_CtdlswEventMaxEntries_Type())
ctdlswEventMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventMaxEntries.setStatus(_A)
class _CtdlswEventTraceAll_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtdlswEventTraceAll_Type.__name__=_C
_CtdlswEventTraceAll_Object=MibScalar
ctdlswEventTraceAll=_CtdlswEventTraceAll_Object((1,3,6,1,4,1,52,4,1,2,8,6,1,3),_CtdlswEventTraceAll_Type())
ctdlswEventTraceAll.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventTraceAll.setStatus(_A)
_CtdlswEventLogFilterTable_ObjectIdentity=ObjectIdentity
ctdlswEventLogFilterTable=_CtdlswEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,6,2))
_CtdlswEventFilterTable_Object=MibTable
ctdlswEventFilterTable=_CtdlswEventFilterTable_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1))
if mibBuilder.loadTexts:ctdlswEventFilterTable.setStatus(_A)
_CtdlswEventFilterEntry_Object=MibTableRow
ctdlswEventFilterEntry=_CtdlswEventFilterEntry_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1))
ctdlswEventFilterEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:ctdlswEventFilterEntry.setStatus(_A)
_CtdlswEventFltrProtocol_Type=Integer32
_CtdlswEventFltrProtocol_Object=MibTableColumn
ctdlswEventFltrProtocol=_CtdlswEventFltrProtocol_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,1),_CtdlswEventFltrProtocol_Type())
ctdlswEventFltrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventFltrProtocol.setStatus(_A)
_CtdlswEventFltrIfNum_Type=Integer32
_CtdlswEventFltrIfNum_Object=MibTableColumn
ctdlswEventFltrIfNum=_CtdlswEventFltrIfNum_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,2),_CtdlswEventFltrIfNum_Type())
ctdlswEventFltrIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventFltrIfNum.setStatus(_A)
class _CtdlswEventFltrControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),('add',3)))
_CtdlswEventFltrControl_Type.__name__=_C
_CtdlswEventFltrControl_Object=MibTableColumn
ctdlswEventFltrControl=_CtdlswEventFltrControl_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,3),_CtdlswEventFltrControl_Type())
ctdlswEventFltrControl.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventFltrControl.setStatus(_A)
class _CtdlswEventFltrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_CtdlswEventFltrType_Type.__name__=_C
_CtdlswEventFltrType_Object=MibTableColumn
ctdlswEventFltrType=_CtdlswEventFltrType_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,4),_CtdlswEventFltrType_Type())
ctdlswEventFltrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventFltrType.setStatus(_A)
class _CtdlswEventFltrSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3)))
_CtdlswEventFltrSeverity_Type.__name__=_C
_CtdlswEventFltrSeverity_Object=MibTableColumn
ctdlswEventFltrSeverity=_CtdlswEventFltrSeverity_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,5),_CtdlswEventFltrSeverity_Type())
ctdlswEventFltrSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventFltrSeverity.setStatus(_A)
class _CtdlswEventFltrAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('logTrap',3)))
_CtdlswEventFltrAction_Type.__name__=_C
_CtdlswEventFltrAction_Object=MibTableColumn
ctdlswEventFltrAction=_CtdlswEventFltrAction_Object((1,3,6,1,4,1,52,4,1,2,8,6,2,1,1,6),_CtdlswEventFltrAction_Type())
ctdlswEventFltrAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ctdlswEventFltrAction.setStatus(_A)
_CtdlswEventLogTable_ObjectIdentity=ObjectIdentity
ctdlswEventLogTable=_CtdlswEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,8,6,3))
_CtdlswEventTable_Object=MibTable
ctdlswEventTable=_CtdlswEventTable_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1))
if mibBuilder.loadTexts:ctdlswEventTable.setStatus(_A)
_CtdlswEventEntry_Object=MibTableRow
ctdlswEventEntry=_CtdlswEventEntry_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1))
ctdlswEventEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:ctdlswEventEntry.setStatus(_A)
_CtdlswEventNumber_Type=Integer32
_CtdlswEventNumber_Object=MibTableColumn
ctdlswEventNumber=_CtdlswEventNumber_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,1),_CtdlswEventNumber_Type())
ctdlswEventNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventNumber.setStatus(_A)
_CtdlswEventTime_Type=TimeTicks
_CtdlswEventTime_Object=MibTableColumn
ctdlswEventTime=_CtdlswEventTime_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,2),_CtdlswEventTime_Type())
ctdlswEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventTime.setStatus(_A)
class _CtdlswEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_CtdlswEventType_Type.__name__=_C
_CtdlswEventType_Object=MibTableColumn
ctdlswEventType=_CtdlswEventType_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,3),_CtdlswEventType_Type())
ctdlswEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventType.setStatus(_A)
class _CtdlswEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3)))
_CtdlswEventSeverity_Type.__name__=_C
_CtdlswEventSeverity_Object=MibTableColumn
ctdlswEventSeverity=_CtdlswEventSeverity_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,4),_CtdlswEventSeverity_Type())
ctdlswEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventSeverity.setStatus(_A)
_CtdlswEventProtocol_Type=Integer32
_CtdlswEventProtocol_Object=MibTableColumn
ctdlswEventProtocol=_CtdlswEventProtocol_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,5),_CtdlswEventProtocol_Type())
ctdlswEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventProtocol.setStatus(_A)
_CtdlswEventIfNum_Type=Integer32
_CtdlswEventIfNum_Object=MibTableColumn
ctdlswEventIfNum=_CtdlswEventIfNum_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,6),_CtdlswEventIfNum_Type())
ctdlswEventIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventIfNum.setStatus(_A)
_CtdlswEventTextString_Type=OctetString
_CtdlswEventTextString_Object=MibTableColumn
ctdlswEventTextString=_CtdlswEventTextString_Object((1,3,6,1,4,1,52,4,1,2,8,6,3,1,1,7),_CtdlswEventTextString_Type())
ctdlswEventTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:ctdlswEventTextString.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'NBName':NBName,'ctdlswNode':ctdlswNode,'ctdlswNodeConfig':ctdlswNodeConfig,'ctdlswVersion':ctdlswVersion,'ctdlswAdminStatus':ctdlswAdminStatus,'ctdlswOperStatus':ctdlswOperStatus,'ctdlswUpTime':ctdlswUpTime,'ctdlswOperVirtualRingNumber':ctdlswOperVirtualRingNumber,'ctdlswNBLocalFilterType':ctdlswNBLocalFilterType,'ctdlswNBRemoteFilterType':ctdlswNBRemoteFilterType,'ctdlswMacLocalFilterType':ctdlswMacLocalFilterType,'ctdlswMacRemoteFilterType':ctdlswMacRemoteFilterType,'ctdlswAcceptDynamicTConn':ctdlswAcceptDynamicTConn,'ctdlswDefaultPortNumber':ctdlswDefaultPortNumber,'ctdlswPort':ctdlswPort,'ctdlswPortTable':ctdlswPortTable,'ctdlswPortEntry':ctdlswPortEntry,'ctdlswPortIndex':ctdlswPortIndex,_N:ctdlswPortName,'ctdlswPortAddress':ctdlswPortAddress,'ctdlswPortAdminStatus':ctdlswPortAdminStatus,'ctdlswPortOperStatus':ctdlswPortOperStatus,'ctdlswPortUpTime':ctdlswPortUpTime,'ctdlswFilter':ctdlswFilter,'ctdlswLocalNBFilterTable':ctdlswLocalNBFilterTable,'ctdlswLocalNBFilterEntry':ctdlswLocalNBFilterEntry,_O:ctdlswLocalNBFilterSrcName,_P:ctdlswLocalNBFilterDestName,'ctdlswLocalNBFilterControl':ctdlswLocalNBFilterControl,'ctdlswRemoteNBFilterTable':ctdlswRemoteNBFilterTable,'ctdlswRemoteNBFilterEntry':ctdlswRemoteNBFilterEntry,_Q:ctdlswRemoteNBFilterSrcName,_R:ctdlswRemoteNBFilterDestName,'ctdlswRemoteNBFilterControl':ctdlswRemoteNBFilterControl,'ctdlswLocalMacFilterTable':ctdlswLocalMacFilterTable,'ctdlswLocalMacFilterEntry':ctdlswLocalMacFilterEntry,_S:ctdlswLocalMacFilterSrcAddr,_T:ctdlswLocalMacFilterSrcMask,_U:ctdlswLocalMacFilterDestAddr,_V:ctdlswLocalMacFilterDestMask,'ctdlswLocalMacFilterControl':ctdlswLocalMacFilterControl,'ctdlswRemoteMacFilterTable':ctdlswRemoteMacFilterTable,'ctdlswRemoteMacFilterEntry':ctdlswRemoteMacFilterEntry,_W:ctdlswRemoteMacFilterSrcAddr,_X:ctdlswRemoteMacFilterSrcMask,_Y:ctdlswRemoteMacFilterDestAddr,_Z:ctdlswRemoteMacFilterDestMask,'ctdlswRemoteMacFilterControl':ctdlswRemoteMacFilterControl,'ctdlswTConn':ctdlswTConn,'ctdlswTConnTable':ctdlswTConnTable,'ctdlswTConnEntry':ctdlswTConnEntry,_a:ctdlswTConnRemoteTAddr,'ctdlswTConnControl':ctdlswTConnControl,'ctdlswTConnUpTime':ctdlswTConnUpTime,'ctdlswTConnOperStatus':ctdlswTConnOperStatus,'ctdlswTConnType':ctdlswTConnType,'ctdlswTrap':ctdlswTrap,'ctdlswEvent':ctdlswEvent,'ctdlswEventLogConfig':ctdlswEventLogConfig,'ctdlswEventAdminStatus':ctdlswEventAdminStatus,'ctdlswEventMaxEntries':ctdlswEventMaxEntries,'ctdlswEventTraceAll':ctdlswEventTraceAll,'ctdlswEventLogFilterTable':ctdlswEventLogFilterTable,'ctdlswEventFilterTable':ctdlswEventFilterTable,'ctdlswEventFilterEntry':ctdlswEventFilterEntry,_b:ctdlswEventFltrProtocol,_c:ctdlswEventFltrIfNum,'ctdlswEventFltrControl':ctdlswEventFltrControl,'ctdlswEventFltrType':ctdlswEventFltrType,'ctdlswEventFltrSeverity':ctdlswEventFltrSeverity,'ctdlswEventFltrAction':ctdlswEventFltrAction,'ctdlswEventLogTable':ctdlswEventLogTable,'ctdlswEventTable':ctdlswEventTable,'ctdlswEventEntry':ctdlswEventEntry,_g:ctdlswEventNumber,'ctdlswEventTime':ctdlswEventTime,'ctdlswEventType':ctdlswEventType,'ctdlswEventSeverity':ctdlswEventSeverity,'ctdlswEventProtocol':ctdlswEventProtocol,'ctdlswEventIfNum':ctdlswEventIfNum,'ctdlswEventTextString':ctdlswEventTextString})