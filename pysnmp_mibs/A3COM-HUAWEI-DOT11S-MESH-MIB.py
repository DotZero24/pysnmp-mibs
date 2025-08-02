_V='h3cDot11sMeshNbrIndex'
_U='h3cDot11sMeshLinkStatIfIndex'
_T='h3cDot11sMeshLinkIfIndex'
_S='h3cDot11sWDSPeerMacIndex'
_R='h3cDot11sMlspProxyIndex'
_Q='millisecond'
_P='h3cDot11sMeshPflIndex'
_O='h3cDot11sCfgRadioIndex'
_N='dBm'
_M='h3cDot11sMpPlcyIndex'
_L='second'
_K='read-write'
_J='h3cDot11APElementIndex'
_I='A3COM-HUAWEI-DOT11-REF-MIB'
_H='OctetString'
_G='TruthValue'
_F='not-accessible'
_E='A3COM-HUAWEI-DOT11S-MESH-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11RadioElementIndex,h3cDot11,h3cDot11APElementIndex=mibBuilder.importSymbols(_I,'H3cDot11RadioElementIndex','h3cDot11',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
h3cDot11sMesh=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,75,11))
if mibBuilder.loadTexts:h3cDot11sMesh.setRevisions(('2009-08-01 10:00','2008-11-07 10:00','2008-07-08 18:00'))
_H3cDot11sConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11sConfigGroup=_H3cDot11sConfigGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,11,1))
_H3cDot11sMeshGlobalPara_ObjectIdentity=ObjectIdentity
h3cDot11sMeshGlobalPara=_H3cDot11sMeshGlobalPara_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,11,1,1))
_H3cDot11sMeshMkdID_Type=MacAddress
_H3cDot11sMeshMkdID_Object=MibScalar
h3cDot11sMeshMkdID=_H3cDot11sMeshMkdID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,1,1),_H3cDot11sMeshMkdID_Type())
h3cDot11sMeshMkdID.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11sMeshMkdID.setStatus(_A)
_H3cDot11sMeshPflTable_Object=MibTable
h3cDot11sMeshPflTable=_H3cDot11sMeshPflTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2))
if mibBuilder.loadTexts:h3cDot11sMeshPflTable.setStatus(_A)
_H3cDot11sMeshPflEntry_Object=MibTableRow
h3cDot11sMeshPflEntry=_H3cDot11sMeshPflEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1))
h3cDot11sMeshPflEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:h3cDot11sMeshPflEntry.setStatus(_A)
_H3cDot11sMeshPflIndex_Type=Integer32
_H3cDot11sMeshPflIndex_Object=MibTableColumn
h3cDot11sMeshPflIndex=_H3cDot11sMeshPflIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,1),_H3cDot11sMeshPflIndex_Type())
h3cDot11sMeshPflIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMeshPflIndex.setStatus(_A)
class _H3cDot11sMeshPflMeshID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDot11sMeshPflMeshID_Type.__name__=_H
_H3cDot11sMeshPflMeshID_Object=MibTableColumn
h3cDot11sMeshPflMeshID=_H3cDot11sMeshPflMeshID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,2),_H3cDot11sMeshPflMeshID_Type())
h3cDot11sMeshPflMeshID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflMeshID.setStatus(_A)
class _H3cDot11sMeshPflBindIntNum_Type(Integer32):defaultValue=-1
_H3cDot11sMeshPflBindIntNum_Type.__name__=_D
_H3cDot11sMeshPflBindIntNum_Object=MibTableColumn
h3cDot11sMeshPflBindIntNum=_H3cDot11sMeshPflBindIntNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,3),_H3cDot11sMeshPflBindIntNum_Type())
h3cDot11sMeshPflBindIntNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflBindIntNum.setStatus(_A)
class _H3cDot11sMeshPflKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_H3cDot11sMeshPflKeepAlive_Type.__name__=_D
_H3cDot11sMeshPflKeepAlive_Object=MibTableColumn
h3cDot11sMeshPflKeepAlive=_H3cDot11sMeshPflKeepAlive_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,4),_H3cDot11sMeshPflKeepAlive_Type())
h3cDot11sMeshPflKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sMeshPflKeepAlive.setUnits(_L)
_H3cDot11sMeshPflBackhaulRate_Type=Integer32
_H3cDot11sMeshPflBackhaulRate_Object=MibTableColumn
h3cDot11sMeshPflBackhaulRate=_H3cDot11sMeshPflBackhaulRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,5),_H3cDot11sMeshPflBackhaulRate_Type())
h3cDot11sMeshPflBackhaulRate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflBackhaulRate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sMeshPflBackhaulRate.setUnits('Kbps')
class _H3cDot11sMeshMkdServEnable_Type(TruthValue):defaultValue=2
_H3cDot11sMeshMkdServEnable_Type.__name__=_G
_H3cDot11sMeshMkdServEnable_Object=MibTableColumn
h3cDot11sMeshMkdServEnable=_H3cDot11sMeshMkdServEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,6),_H3cDot11sMeshMkdServEnable_Type())
h3cDot11sMeshMkdServEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshMkdServEnable.setStatus(_A)
class _H3cDot11sMeshPflEnable_Type(TruthValue):defaultValue=2
_H3cDot11sMeshPflEnable_Type.__name__=_G
_H3cDot11sMeshPflEnable_Object=MibTableColumn
h3cDot11sMeshPflEnable=_H3cDot11sMeshPflEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,7),_H3cDot11sMeshPflEnable_Type())
h3cDot11sMeshPflEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflEnable.setStatus(_A)
_H3cDot11sMeshPflRowStatus_Type=RowStatus
_H3cDot11sMeshPflRowStatus_Object=MibTableColumn
h3cDot11sMeshPflRowStatus=_H3cDot11sMeshPflRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,2,1,8),_H3cDot11sMeshPflRowStatus_Type())
h3cDot11sMeshPflRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMeshPflRowStatus.setStatus(_A)
_H3cDot11sMpPlcyTable_Object=MibTable
h3cDot11sMpPlcyTable=_H3cDot11sMpPlcyTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3))
if mibBuilder.loadTexts:h3cDot11sMpPlcyTable.setStatus(_A)
_H3cDot11sMpPlcyEntry_Object=MibTableRow
h3cDot11sMpPlcyEntry=_H3cDot11sMpPlcyEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1))
h3cDot11sMpPlcyEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:h3cDot11sMpPlcyEntry.setStatus(_A)
_H3cDot11sMpPlcyIndex_Type=Integer32
_H3cDot11sMpPlcyIndex_Object=MibTableColumn
h3cDot11sMpPlcyIndex=_H3cDot11sMpPlcyIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,1),_H3cDot11sMpPlcyIndex_Type())
h3cDot11sMpPlcyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMpPlcyIndex.setStatus(_A)
class _H3cDot11sMpPlcyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cDot11sMpPlcyName_Type.__name__=_H
_H3cDot11sMpPlcyName_Object=MibTableColumn
h3cDot11sMpPlcyName=_H3cDot11sMpPlcyName_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,2),_H3cDot11sMpPlcyName_Type())
h3cDot11sMpPlcyName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMpPlcyName.setStatus(_A)
class _H3cDot11sMpPlcyInitEnable_Type(TruthValue):defaultValue=1
_H3cDot11sMpPlcyInitEnable_Type.__name__=_G
_H3cDot11sMpPlcyInitEnable_Object=MibTableColumn
h3cDot11sMpPlcyInitEnable=_H3cDot11sMpPlcyInitEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,3),_H3cDot11sMpPlcyInitEnable_Type())
h3cDot11sMpPlcyInitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMpPlcyInitEnable.setStatus(_A)
class _H3cDot11sMlspEnable_Type(TruthValue):defaultValue=2
_H3cDot11sMlspEnable_Type.__name__=_G
_H3cDot11sMlspEnable_Object=MibTableColumn
h3cDot11sMlspEnable=_H3cDot11sMlspEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,4),_H3cDot11sMlspEnable_Type())
h3cDot11sMlspEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMlspEnable.setStatus(_A)
_H3cDot11sProbReqInterval_Type=Integer32
_H3cDot11sProbReqInterval_Object=MibTableColumn
h3cDot11sProbReqInterval=_H3cDot11sProbReqInterval_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,5),_H3cDot11sProbReqInterval_Type())
h3cDot11sProbReqInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sProbReqInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sProbReqInterval.setUnits(_Q)
class _H3cDot11sRoleAuthEnable_Type(TruthValue):defaultValue=1
_H3cDot11sRoleAuthEnable_Type.__name__=_G
_H3cDot11sRoleAuthEnable_Object=MibTableColumn
h3cDot11sRoleAuthEnable=_H3cDot11sRoleAuthEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,6),_H3cDot11sRoleAuthEnable_Type())
h3cDot11sRoleAuthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sRoleAuthEnable.setStatus(_A)
class _H3cDot11sLinkHoldRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,100))
_H3cDot11sLinkHoldRSSI_Type.__name__=_D
_H3cDot11sLinkHoldRSSI_Object=MibTableColumn
h3cDot11sLinkHoldRSSI=_H3cDot11sLinkHoldRSSI_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,7),_H3cDot11sLinkHoldRSSI_Type())
h3cDot11sLinkHoldRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sLinkHoldRSSI.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sLinkHoldRSSI.setUnits(_N)
class _H3cDot11sLinkHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,20000))
_H3cDot11sLinkHoldTime_Type.__name__=_D
_H3cDot11sLinkHoldTime_Object=MibTableColumn
h3cDot11sLinkHoldTime=_H3cDot11sLinkHoldTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,8),_H3cDot11sLinkHoldTime_Type())
h3cDot11sLinkHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sLinkHoldTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sLinkHoldTime.setUnits(_Q)
class _H3cDot11sSwitchMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cDot11sSwitchMargin_Type.__name__=_D
_H3cDot11sSwitchMargin_Object=MibTableColumn
h3cDot11sSwitchMargin=_H3cDot11sSwitchMargin_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,9),_H3cDot11sSwitchMargin_Type())
h3cDot11sSwitchMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sSwitchMargin.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sSwitchMargin.setUnits(_N)
class _H3cDot11sLinkSaturationRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,150))
_H3cDot11sLinkSaturationRSSI_Type.__name__=_D
_H3cDot11sLinkSaturationRSSI_Object=MibTableColumn
h3cDot11sLinkSaturationRSSI=_H3cDot11sLinkSaturationRSSI_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,10),_H3cDot11sLinkSaturationRSSI_Type())
h3cDot11sLinkSaturationRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sLinkSaturationRSSI.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sLinkSaturationRSSI.setUnits(_N)
class _H3cDot11sLinkRateMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('realtime',2)))
_H3cDot11sLinkRateMode_Type.__name__=_D
_H3cDot11sLinkRateMode_Object=MibTableColumn
h3cDot11sLinkRateMode=_H3cDot11sLinkRateMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,11),_H3cDot11sLinkRateMode_Type())
h3cDot11sLinkRateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sLinkRateMode.setStatus(_A)
_H3cDot11sMaxLinkNum_Type=Integer32
_H3cDot11sMaxLinkNum_Object=MibTableColumn
h3cDot11sMaxLinkNum=_H3cDot11sMaxLinkNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,12),_H3cDot11sMaxLinkNum_Type())
h3cDot11sMaxLinkNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMaxLinkNum.setStatus(_A)
_H3cDot11sMpPlcyRowStatus_Type=RowStatus
_H3cDot11sMpPlcyRowStatus_Object=MibTableColumn
h3cDot11sMpPlcyRowStatus=_H3cDot11sMpPlcyRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,3,1,13),_H3cDot11sMpPlcyRowStatus_Type())
h3cDot11sMpPlcyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMpPlcyRowStatus.setStatus(_A)
_H3cDot11sMlspCfgTable_Object=MibTable
h3cDot11sMlspCfgTable=_H3cDot11sMlspCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,4))
if mibBuilder.loadTexts:h3cDot11sMlspCfgTable.setStatus(_A)
_H3cDot11sMlspCfgEntry_Object=MibTableRow
h3cDot11sMlspCfgEntry=_H3cDot11sMlspCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,4,1))
h3cDot11sMlspCfgEntry.setIndexNames((0,_E,_M),(0,_E,_R))
if mibBuilder.loadTexts:h3cDot11sMlspCfgEntry.setStatus(_A)
_H3cDot11sMlspProxyIndex_Type=Integer32
_H3cDot11sMlspProxyIndex_Object=MibTableColumn
h3cDot11sMlspProxyIndex=_H3cDot11sMlspProxyIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,4,1,1),_H3cDot11sMlspProxyIndex_Type())
h3cDot11sMlspProxyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMlspProxyIndex.setStatus(_A)
_H3cDot11sMlspProxyMac_Type=MacAddress
_H3cDot11sMlspProxyMac_Object=MibTableColumn
h3cDot11sMlspProxyMac=_H3cDot11sMlspProxyMac_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,4,1,2),_H3cDot11sMlspProxyMac_Type())
h3cDot11sMlspProxyMac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMlspProxyMac.setStatus(_A)
_H3cDot11sMlspRowStatus_Type=RowStatus
_H3cDot11sMlspRowStatus_Object=MibTableColumn
h3cDot11sMlspRowStatus=_H3cDot11sMlspRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,4,1,3),_H3cDot11sMlspRowStatus_Type())
h3cDot11sMlspRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sMlspRowStatus.setStatus(_A)
_H3cDot11sRadioCfgTable_Object=MibTable
h3cDot11sRadioCfgTable=_H3cDot11sRadioCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,5))
if mibBuilder.loadTexts:h3cDot11sRadioCfgTable.setStatus(_A)
_H3cDot11sRadioCfgEntry_Object=MibTableRow
h3cDot11sRadioCfgEntry=_H3cDot11sRadioCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,5,1))
h3cDot11sRadioCfgEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:h3cDot11sRadioCfgEntry.setStatus(_A)
_H3cDot11sCfgRadioIndex_Type=H3cDot11RadioElementIndex
_H3cDot11sCfgRadioIndex_Object=MibTableColumn
h3cDot11sCfgRadioIndex=_H3cDot11sCfgRadioIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,5,1,1),_H3cDot11sCfgRadioIndex_Type())
h3cDot11sCfgRadioIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sCfgRadioIndex.setStatus(_A)
class _H3cDot11sMeshPflMap_Type(Integer32):defaultValue=0
_H3cDot11sMeshPflMap_Type.__name__=_D
_H3cDot11sMeshPflMap_Object=MibTableColumn
h3cDot11sMeshPflMap=_H3cDot11sMeshPflMap_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,5,1,2),_H3cDot11sMeshPflMap_Type())
h3cDot11sMeshPflMap.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11sMeshPflMap.setStatus(_A)
class _H3cDot11sMpPlcyMap_Type(Integer32):defaultValue=1
_H3cDot11sMpPlcyMap_Type.__name__=_D
_H3cDot11sMpPlcyMap_Object=MibTableColumn
h3cDot11sMpPlcyMap=_H3cDot11sMpPlcyMap_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,5,1,3),_H3cDot11sMpPlcyMap_Type())
h3cDot11sMpPlcyMap.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11sMpPlcyMap.setStatus(_A)
_H3cDot11sAPCfgTable_Object=MibTable
h3cDot11sAPCfgTable=_H3cDot11sAPCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,6))
if mibBuilder.loadTexts:h3cDot11sAPCfgTable.setStatus(_A)
_H3cDot11sAPCfgEntry_Object=MibTableRow
h3cDot11sAPCfgEntry=_H3cDot11sAPCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,6,1))
h3cDot11sAPCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cDot11sAPCfgEntry.setStatus(_A)
class _H3cDot11sPortalEnable_Type(TruthValue):defaultValue=2
_H3cDot11sPortalEnable_Type.__name__=_G
_H3cDot11sPortalEnable_Object=MibTableColumn
h3cDot11sPortalEnable=_H3cDot11sPortalEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,1,6,1,1),_H3cDot11sPortalEnable_Type())
h3cDot11sPortalEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11sPortalEnable.setStatus(_A)
_H3cDot11sWDSConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11sWDSConfigGroup=_H3cDot11sWDSConfigGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,11,2))
_H3cDot11sWDSPeerMacTable_Object=MibTable
h3cDot11sWDSPeerMacTable=_H3cDot11sWDSPeerMacTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,2,1))
if mibBuilder.loadTexts:h3cDot11sWDSPeerMacTable.setStatus(_A)
_H3cDot11sWDSPeerMacEntry_Object=MibTableRow
h3cDot11sWDSPeerMacEntry=_H3cDot11sWDSPeerMacEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,2,1,1))
h3cDot11sWDSPeerMacEntry.setIndexNames((0,_E,_O),(0,_E,_S))
if mibBuilder.loadTexts:h3cDot11sWDSPeerMacEntry.setStatus(_A)
_H3cDot11sWDSPeerMacIndex_Type=Integer32
_H3cDot11sWDSPeerMacIndex_Object=MibTableColumn
h3cDot11sWDSPeerMacIndex=_H3cDot11sWDSPeerMacIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,2,1,1,1),_H3cDot11sWDSPeerMacIndex_Type())
h3cDot11sWDSPeerMacIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sWDSPeerMacIndex.setStatus(_A)
_H3cDot11sWDSPeerMacAddrss_Type=MacAddress
_H3cDot11sWDSPeerMacAddrss_Object=MibTableColumn
h3cDot11sWDSPeerMacAddrss=_H3cDot11sWDSPeerMacAddrss_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,2,1,1,2),_H3cDot11sWDSPeerMacAddrss_Type())
h3cDot11sWDSPeerMacAddrss.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sWDSPeerMacAddrss.setStatus(_A)
_H3cDot11sWDSPeerMacRowStatus_Type=RowStatus
_H3cDot11sWDSPeerMacRowStatus_Object=MibTableColumn
h3cDot11sWDSPeerMacRowStatus=_H3cDot11sWDSPeerMacRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,2,1,1,3),_H3cDot11sWDSPeerMacRowStatus_Type())
h3cDot11sWDSPeerMacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11sWDSPeerMacRowStatus.setStatus(_A)
_H3cDot11sMeshStatusGroup_ObjectIdentity=ObjectIdentity
h3cDot11sMeshStatusGroup=_H3cDot11sMeshStatusGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,11,3))
_H3cDot11sMeshLinkStatusTable_Object=MibTable
h3cDot11sMeshLinkStatusTable=_H3cDot11sMeshLinkStatusTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1))
if mibBuilder.loadTexts:h3cDot11sMeshLinkStatusTable.setStatus(_A)
_H3cDot11sMeshLinkStatusEntry_Object=MibTableRow
h3cDot11sMeshLinkStatusEntry=_H3cDot11sMeshLinkStatusEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1))
h3cDot11sMeshLinkStatusEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:h3cDot11sMeshLinkStatusEntry.setStatus(_A)
_H3cDot11sMeshLinkIfIndex_Type=Unsigned32
_H3cDot11sMeshLinkIfIndex_Object=MibTableColumn
h3cDot11sMeshLinkIfIndex=_H3cDot11sMeshLinkIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1,1),_H3cDot11sMeshLinkIfIndex_Type())
h3cDot11sMeshLinkIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMeshLinkIfIndex.setStatus(_A)
_H3cDot11sMeshLinkName_Type=OctetString
_H3cDot11sMeshLinkName_Object=MibTableColumn
h3cDot11sMeshLinkName=_H3cDot11sMeshLinkName_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1,2),_H3cDot11sMeshLinkName_Type())
h3cDot11sMeshLinkName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkName.setStatus(_A)
_H3cDot11sMeshLinkBSSID_Type=MacAddress
_H3cDot11sMeshLinkBSSID_Object=MibTableColumn
h3cDot11sMeshLinkBSSID=_H3cDot11sMeshLinkBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1,3),_H3cDot11sMeshLinkBSSID_Type())
h3cDot11sMeshLinkBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkBSSID.setStatus(_A)
_H3cDot11sMeshLinkPeerMac_Type=MacAddress
_H3cDot11sMeshLinkPeerMac_Object=MibTableColumn
h3cDot11sMeshLinkPeerMac=_H3cDot11sMeshLinkPeerMac_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1,4),_H3cDot11sMeshLinkPeerMac_Type())
h3cDot11sMeshLinkPeerMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkPeerMac.setStatus(_A)
_H3cDot11sMeshLinkExistDuration_Type=Integer32
_H3cDot11sMeshLinkExistDuration_Object=MibTableColumn
h3cDot11sMeshLinkExistDuration=_H3cDot11sMeshLinkExistDuration_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,1,1,5),_H3cDot11sMeshLinkExistDuration_Type())
h3cDot11sMeshLinkExistDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkExistDuration.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sMeshLinkExistDuration.setUnits(_L)
_H3cDot11sMeshLinkStatisTable_Object=MibTable
h3cDot11sMeshLinkStatisTable=_H3cDot11sMeshLinkStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2))
if mibBuilder.loadTexts:h3cDot11sMeshLinkStatisTable.setStatus(_A)
_H3cDot11sMeshLinkStatisEntry_Object=MibTableRow
h3cDot11sMeshLinkStatisEntry=_H3cDot11sMeshLinkStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1))
h3cDot11sMeshLinkStatisEntry.setIndexNames((0,_I,_J),(0,_E,_U))
if mibBuilder.loadTexts:h3cDot11sMeshLinkStatisEntry.setStatus(_A)
_H3cDot11sMeshLinkStatIfIndex_Type=Unsigned32
_H3cDot11sMeshLinkStatIfIndex_Object=MibTableColumn
h3cDot11sMeshLinkStatIfIndex=_H3cDot11sMeshLinkStatIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,1),_H3cDot11sMeshLinkStatIfIndex_Type())
h3cDot11sMeshLinkStatIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMeshLinkStatIfIndex.setStatus(_A)
_H3cDot11sMeshLinkNbrIndex_Type=Unsigned32
_H3cDot11sMeshLinkNbrIndex_Object=MibTableColumn
h3cDot11sMeshLinkNbrIndex=_H3cDot11sMeshLinkNbrIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,2),_H3cDot11sMeshLinkNbrIndex_Type())
h3cDot11sMeshLinkNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkNbrIndex.setStatus(_A)
_H3cDot11sMeshLinkRxTotByte_Type=Counter32
_H3cDot11sMeshLinkRxTotByte_Object=MibTableColumn
h3cDot11sMeshLinkRxTotByte=_H3cDot11sMeshLinkRxTotByte_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,3),_H3cDot11sMeshLinkRxTotByte_Type())
h3cDot11sMeshLinkRxTotByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxTotByte.setStatus(_A)
_H3cDot11sMeshLinkRxTotPkt_Type=Counter32
_H3cDot11sMeshLinkRxTotPkt_Object=MibTableColumn
h3cDot11sMeshLinkRxTotPkt=_H3cDot11sMeshLinkRxTotPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,4),_H3cDot11sMeshLinkRxTotPkt_Type())
h3cDot11sMeshLinkRxTotPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxTotPkt.setStatus(_A)
_H3cDot11sMeshLinkRxUniPkt_Type=Counter32
_H3cDot11sMeshLinkRxUniPkt_Object=MibTableColumn
h3cDot11sMeshLinkRxUniPkt=_H3cDot11sMeshLinkRxUniPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,5),_H3cDot11sMeshLinkRxUniPkt_Type())
h3cDot11sMeshLinkRxUniPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxUniPkt.setStatus(_A)
_H3cDot11sMeshLinkRxBrocPkt_Type=Counter32
_H3cDot11sMeshLinkRxBrocPkt_Object=MibTableColumn
h3cDot11sMeshLinkRxBrocPkt=_H3cDot11sMeshLinkRxBrocPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,6),_H3cDot11sMeshLinkRxBrocPkt_Type())
h3cDot11sMeshLinkRxBrocPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxBrocPkt.setStatus(_A)
_H3cDot11sMeshLinkRxMuticPkt_Type=Counter32
_H3cDot11sMeshLinkRxMuticPkt_Object=MibTableColumn
h3cDot11sMeshLinkRxMuticPkt=_H3cDot11sMeshLinkRxMuticPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,7),_H3cDot11sMeshLinkRxMuticPkt_Type())
h3cDot11sMeshLinkRxMuticPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxMuticPkt.setStatus(_A)
_H3cDot11sMeshLinkRxDiscPkt_Type=Counter32
_H3cDot11sMeshLinkRxDiscPkt_Object=MibTableColumn
h3cDot11sMeshLinkRxDiscPkt=_H3cDot11sMeshLinkRxDiscPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,8),_H3cDot11sMeshLinkRxDiscPkt_Type())
h3cDot11sMeshLinkRxDiscPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkRxDiscPkt.setStatus(_A)
_H3cDot11sMeshLinkTxTotByte_Type=Counter32
_H3cDot11sMeshLinkTxTotByte_Object=MibTableColumn
h3cDot11sMeshLinkTxTotByte=_H3cDot11sMeshLinkTxTotByte_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,9),_H3cDot11sMeshLinkTxTotByte_Type())
h3cDot11sMeshLinkTxTotByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxTotByte.setStatus(_A)
_H3cDot11sMeshLinkTxTotPkt_Type=Counter32
_H3cDot11sMeshLinkTxTotPkt_Object=MibTableColumn
h3cDot11sMeshLinkTxTotPkt=_H3cDot11sMeshLinkTxTotPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,10),_H3cDot11sMeshLinkTxTotPkt_Type())
h3cDot11sMeshLinkTxTotPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxTotPkt.setStatus(_A)
_H3cDot11sMeshLinkTxUniPkt_Type=Counter32
_H3cDot11sMeshLinkTxUniPkt_Object=MibTableColumn
h3cDot11sMeshLinkTxUniPkt=_H3cDot11sMeshLinkTxUniPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,11),_H3cDot11sMeshLinkTxUniPkt_Type())
h3cDot11sMeshLinkTxUniPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxUniPkt.setStatus(_A)
_H3cDot11sMeshLinkTxBrocPkt_Type=Counter32
_H3cDot11sMeshLinkTxBrocPkt_Object=MibTableColumn
h3cDot11sMeshLinkTxBrocPkt=_H3cDot11sMeshLinkTxBrocPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,12),_H3cDot11sMeshLinkTxBrocPkt_Type())
h3cDot11sMeshLinkTxBrocPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxBrocPkt.setStatus(_A)
_H3cDot11sMeshLinkTxMuticPkt_Type=Counter32
_H3cDot11sMeshLinkTxMuticPkt_Object=MibTableColumn
h3cDot11sMeshLinkTxMuticPkt=_H3cDot11sMeshLinkTxMuticPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,13),_H3cDot11sMeshLinkTxMuticPkt_Type())
h3cDot11sMeshLinkTxMuticPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxMuticPkt.setStatus(_A)
_H3cDot11sMeshLinkTxDiscPkt_Type=Counter32
_H3cDot11sMeshLinkTxDiscPkt_Object=MibTableColumn
h3cDot11sMeshLinkTxDiscPkt=_H3cDot11sMeshLinkTxDiscPkt_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,14),_H3cDot11sMeshLinkTxDiscPkt_Type())
h3cDot11sMeshLinkTxDiscPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkTxDiscPkt.setStatus(_A)
_H3cDot11sMeshLinkIFName_Type=OctetString
_H3cDot11sMeshLinkIFName_Object=MibTableColumn
h3cDot11sMeshLinkIFName=_H3cDot11sMeshLinkIFName_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,2,1,15),_H3cDot11sMeshLinkIFName_Type())
h3cDot11sMeshLinkIFName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkIFName.setStatus(_A)
_H3cDot11sMeshNbrStatusTable_Object=MibTable
h3cDot11sMeshNbrStatusTable=_H3cDot11sMeshNbrStatusTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3))
if mibBuilder.loadTexts:h3cDot11sMeshNbrStatusTable.setStatus(_A)
_H3cDot11sMeshNbrStatusEntry_Object=MibTableRow
h3cDot11sMeshNbrStatusEntry=_H3cDot11sMeshNbrStatusEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1))
h3cDot11sMeshNbrStatusEntry.setIndexNames((0,_I,_J),(0,_E,_V))
if mibBuilder.loadTexts:h3cDot11sMeshNbrStatusEntry.setStatus(_A)
_H3cDot11sMeshNbrIndex_Type=Unsigned32
_H3cDot11sMeshNbrIndex_Object=MibTableColumn
h3cDot11sMeshNbrIndex=_H3cDot11sMeshNbrIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,1),_H3cDot11sMeshNbrIndex_Type())
h3cDot11sMeshNbrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11sMeshNbrIndex.setStatus(_A)
_H3cDot11sMeshNbrRadioID_Type=Unsigned32
_H3cDot11sMeshNbrRadioID_Object=MibTableColumn
h3cDot11sMeshNbrRadioID=_H3cDot11sMeshNbrRadioID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,2),_H3cDot11sMeshNbrRadioID_Type())
h3cDot11sMeshNbrRadioID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrRadioID.setStatus(_A)
class _H3cDot11sMeshLocalMeshID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDot11sMeshLocalMeshID_Type.__name__=_H
_H3cDot11sMeshLocalMeshID_Object=MibTableColumn
h3cDot11sMeshLocalMeshID=_H3cDot11sMeshLocalMeshID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,3),_H3cDot11sMeshLocalMeshID_Type())
h3cDot11sMeshLocalMeshID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLocalMeshID.setStatus(_A)
class _H3cDot11sMeshNbrMeshID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDot11sMeshNbrMeshID_Type.__name__=_H
_H3cDot11sMeshNbrMeshID_Object=MibTableColumn
h3cDot11sMeshNbrMeshID=_H3cDot11sMeshNbrMeshID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,4),_H3cDot11sMeshNbrMeshID_Type())
h3cDot11sMeshNbrMeshID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrMeshID.setStatus(_A)
_H3cDot11sMeshNbrBSSID_Type=MacAddress
_H3cDot11sMeshNbrBSSID_Object=MibTableColumn
h3cDot11sMeshNbrBSSID=_H3cDot11sMeshNbrBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,5),_H3cDot11sMeshNbrBSSID_Type())
h3cDot11sMeshNbrBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrBSSID.setStatus(_A)
_H3cDot11sMeshNbrPeerMac_Type=MacAddress
_H3cDot11sMeshNbrPeerMac_Object=MibTableColumn
h3cDot11sMeshNbrPeerMac=_H3cDot11sMeshNbrPeerMac_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,6),_H3cDot11sMeshNbrPeerMac_Type())
h3cDot11sMeshNbrPeerMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrPeerMac.setStatus(_A)
_H3cDot11sMeshLinkInMp_Type=Unsigned32
_H3cDot11sMeshLinkInMp_Object=MibTableColumn
h3cDot11sMeshLinkInMp=_H3cDot11sMeshLinkInMp_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,7),_H3cDot11sMeshLinkInMp_Type())
h3cDot11sMeshLinkInMp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshLinkInMp.setStatus(_A)
class _H3cDot11sMeshMPLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('processing',1),('up',2),('down',3)))
_H3cDot11sMeshMPLinkStatus_Type.__name__=_D
_H3cDot11sMeshMPLinkStatus_Object=MibTableColumn
h3cDot11sMeshMPLinkStatus=_H3cDot11sMeshMPLinkStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,8),_H3cDot11sMeshMPLinkStatus_Type())
h3cDot11sMeshMPLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshMPLinkStatus.setStatus(_A)
_H3cDot11sMeshNbrChannel_Type=Unsigned32
_H3cDot11sMeshNbrChannel_Object=MibTableColumn
h3cDot11sMeshNbrChannel=_H3cDot11sMeshNbrChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,9),_H3cDot11sMeshNbrChannel_Type())
h3cDot11sMeshNbrChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrChannel.setStatus(_A)
_H3cDot11sMeshNbrLinkDuration_Type=Integer32
_H3cDot11sMeshNbrLinkDuration_Object=MibTableColumn
h3cDot11sMeshNbrLinkDuration=_H3cDot11sMeshNbrLinkDuration_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,10),_H3cDot11sMeshNbrLinkDuration_Type())
h3cDot11sMeshNbrLinkDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrLinkDuration.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sMeshNbrLinkDuration.setUnits(_L)
_H3cDot11sMeshNbrRSSI_Type=Integer32
_H3cDot11sMeshNbrRSSI_Object=MibTableColumn
h3cDot11sMeshNbrRSSI=_H3cDot11sMeshNbrRSSI_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,11),_H3cDot11sMeshNbrRSSI_Type())
h3cDot11sMeshNbrRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrRSSI.setStatus(_A)
_H3cDot11sMeshNbrSNR_Type=Integer32
_H3cDot11sMeshNbrSNR_Object=MibTableColumn
h3cDot11sMeshNbrSNR=_H3cDot11sMeshNbrSNR_Object((1,3,6,1,4,1,43,45,1,10,2,75,11,3,3,1,12),_H3cDot11sMeshNbrSNR_Type())
h3cDot11sMeshNbrSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11sMeshNbrSNR.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11sMeshNbrSNR.setUnits('percent')
mibBuilder.exportSymbols(_E,**{'h3cDot11sMesh':h3cDot11sMesh,'h3cDot11sConfigGroup':h3cDot11sConfigGroup,'h3cDot11sMeshGlobalPara':h3cDot11sMeshGlobalPara,'h3cDot11sMeshMkdID':h3cDot11sMeshMkdID,'h3cDot11sMeshPflTable':h3cDot11sMeshPflTable,'h3cDot11sMeshPflEntry':h3cDot11sMeshPflEntry,_P:h3cDot11sMeshPflIndex,'h3cDot11sMeshPflMeshID':h3cDot11sMeshPflMeshID,'h3cDot11sMeshPflBindIntNum':h3cDot11sMeshPflBindIntNum,'h3cDot11sMeshPflKeepAlive':h3cDot11sMeshPflKeepAlive,'h3cDot11sMeshPflBackhaulRate':h3cDot11sMeshPflBackhaulRate,'h3cDot11sMeshMkdServEnable':h3cDot11sMeshMkdServEnable,'h3cDot11sMeshPflEnable':h3cDot11sMeshPflEnable,'h3cDot11sMeshPflRowStatus':h3cDot11sMeshPflRowStatus,'h3cDot11sMpPlcyTable':h3cDot11sMpPlcyTable,'h3cDot11sMpPlcyEntry':h3cDot11sMpPlcyEntry,_M:h3cDot11sMpPlcyIndex,'h3cDot11sMpPlcyName':h3cDot11sMpPlcyName,'h3cDot11sMpPlcyInitEnable':h3cDot11sMpPlcyInitEnable,'h3cDot11sMlspEnable':h3cDot11sMlspEnable,'h3cDot11sProbReqInterval':h3cDot11sProbReqInterval,'h3cDot11sRoleAuthEnable':h3cDot11sRoleAuthEnable,'h3cDot11sLinkHoldRSSI':h3cDot11sLinkHoldRSSI,'h3cDot11sLinkHoldTime':h3cDot11sLinkHoldTime,'h3cDot11sSwitchMargin':h3cDot11sSwitchMargin,'h3cDot11sLinkSaturationRSSI':h3cDot11sLinkSaturationRSSI,'h3cDot11sLinkRateMode':h3cDot11sLinkRateMode,'h3cDot11sMaxLinkNum':h3cDot11sMaxLinkNum,'h3cDot11sMpPlcyRowStatus':h3cDot11sMpPlcyRowStatus,'h3cDot11sMlspCfgTable':h3cDot11sMlspCfgTable,'h3cDot11sMlspCfgEntry':h3cDot11sMlspCfgEntry,_R:h3cDot11sMlspProxyIndex,'h3cDot11sMlspProxyMac':h3cDot11sMlspProxyMac,'h3cDot11sMlspRowStatus':h3cDot11sMlspRowStatus,'h3cDot11sRadioCfgTable':h3cDot11sRadioCfgTable,'h3cDot11sRadioCfgEntry':h3cDot11sRadioCfgEntry,_O:h3cDot11sCfgRadioIndex,'h3cDot11sMeshPflMap':h3cDot11sMeshPflMap,'h3cDot11sMpPlcyMap':h3cDot11sMpPlcyMap,'h3cDot11sAPCfgTable':h3cDot11sAPCfgTable,'h3cDot11sAPCfgEntry':h3cDot11sAPCfgEntry,'h3cDot11sPortalEnable':h3cDot11sPortalEnable,'h3cDot11sWDSConfigGroup':h3cDot11sWDSConfigGroup,'h3cDot11sWDSPeerMacTable':h3cDot11sWDSPeerMacTable,'h3cDot11sWDSPeerMacEntry':h3cDot11sWDSPeerMacEntry,_S:h3cDot11sWDSPeerMacIndex,'h3cDot11sWDSPeerMacAddrss':h3cDot11sWDSPeerMacAddrss,'h3cDot11sWDSPeerMacRowStatus':h3cDot11sWDSPeerMacRowStatus,'h3cDot11sMeshStatusGroup':h3cDot11sMeshStatusGroup,'h3cDot11sMeshLinkStatusTable':h3cDot11sMeshLinkStatusTable,'h3cDot11sMeshLinkStatusEntry':h3cDot11sMeshLinkStatusEntry,_T:h3cDot11sMeshLinkIfIndex,'h3cDot11sMeshLinkName':h3cDot11sMeshLinkName,'h3cDot11sMeshLinkBSSID':h3cDot11sMeshLinkBSSID,'h3cDot11sMeshLinkPeerMac':h3cDot11sMeshLinkPeerMac,'h3cDot11sMeshLinkExistDuration':h3cDot11sMeshLinkExistDuration,'h3cDot11sMeshLinkStatisTable':h3cDot11sMeshLinkStatisTable,'h3cDot11sMeshLinkStatisEntry':h3cDot11sMeshLinkStatisEntry,_U:h3cDot11sMeshLinkStatIfIndex,'h3cDot11sMeshLinkNbrIndex':h3cDot11sMeshLinkNbrIndex,'h3cDot11sMeshLinkRxTotByte':h3cDot11sMeshLinkRxTotByte,'h3cDot11sMeshLinkRxTotPkt':h3cDot11sMeshLinkRxTotPkt,'h3cDot11sMeshLinkRxUniPkt':h3cDot11sMeshLinkRxUniPkt,'h3cDot11sMeshLinkRxBrocPkt':h3cDot11sMeshLinkRxBrocPkt,'h3cDot11sMeshLinkRxMuticPkt':h3cDot11sMeshLinkRxMuticPkt,'h3cDot11sMeshLinkRxDiscPkt':h3cDot11sMeshLinkRxDiscPkt,'h3cDot11sMeshLinkTxTotByte':h3cDot11sMeshLinkTxTotByte,'h3cDot11sMeshLinkTxTotPkt':h3cDot11sMeshLinkTxTotPkt,'h3cDot11sMeshLinkTxUniPkt':h3cDot11sMeshLinkTxUniPkt,'h3cDot11sMeshLinkTxBrocPkt':h3cDot11sMeshLinkTxBrocPkt,'h3cDot11sMeshLinkTxMuticPkt':h3cDot11sMeshLinkTxMuticPkt,'h3cDot11sMeshLinkTxDiscPkt':h3cDot11sMeshLinkTxDiscPkt,'h3cDot11sMeshLinkIFName':h3cDot11sMeshLinkIFName,'h3cDot11sMeshNbrStatusTable':h3cDot11sMeshNbrStatusTable,'h3cDot11sMeshNbrStatusEntry':h3cDot11sMeshNbrStatusEntry,_V:h3cDot11sMeshNbrIndex,'h3cDot11sMeshNbrRadioID':h3cDot11sMeshNbrRadioID,'h3cDot11sMeshLocalMeshID':h3cDot11sMeshLocalMeshID,'h3cDot11sMeshNbrMeshID':h3cDot11sMeshNbrMeshID,'h3cDot11sMeshNbrBSSID':h3cDot11sMeshNbrBSSID,'h3cDot11sMeshNbrPeerMac':h3cDot11sMeshNbrPeerMac,'h3cDot11sMeshLinkInMp':h3cDot11sMeshLinkInMp,'h3cDot11sMeshMPLinkStatus':h3cDot11sMeshMPLinkStatus,'h3cDot11sMeshNbrChannel':h3cDot11sMeshNbrChannel,'h3cDot11sMeshNbrLinkDuration':h3cDot11sMeshNbrLinkDuration,'h3cDot11sMeshNbrRSSI':h3cDot11sMeshNbrRSSI,'h3cDot11sMeshNbrSNR':h3cDot11sMeshNbrSNR})