_N='wwpLeosRstpDomainPortId'
_M='dot1dStpPortOperEdgePort'
_L='RSTP-MIB'
_K='OctetString'
_J='wwpLeosRstpPortId'
_I='read-create'
_H='wwpLeosRstpDomainId'
_G='WWP-LEOS-RSTP-MIB'
_F='dot1dStpPort'
_E='BRIDGE-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,=mibBuilder.importSymbols(_E,_F)
dot1dStpPortOperEdgePort,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosRstpMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,13))
if mibBuilder.loadTexts:wwpLeosRstpMIB.setRevisions(('2011-08-02 00:00','2001-04-03 17:00'))
_WwpLeosRstpMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBObjects=_WwpLeosRstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,1))
_WwpLeosRstpDomain_ObjectIdentity=ObjectIdentity
wwpLeosRstpDomain=_WwpLeosRstpDomain_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,1,1))
class _WwpLeosRstpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('rstp',2),('domain',3),('mstp',4)))
_WwpLeosRstpMode_Type.__name__=_B
_WwpLeosRstpMode_Object=MibScalar
wwpLeosRstpMode=_WwpLeosRstpMode_Object((1,3,6,1,4,1,6141,2,60,13,1,1,1),_WwpLeosRstpMode_Type())
wwpLeosRstpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpMode.setStatus(_A)
_WwpLeosRstpDomainTable_Object=MibTable
wwpLeosRstpDomainTable=_WwpLeosRstpDomainTable_Object((1,3,6,1,4,1,6141,2,60,13,1,1,2))
if mibBuilder.loadTexts:wwpLeosRstpDomainTable.setStatus(_A)
_WwpLeosRstpDomainEntry_Object=MibTableRow
wwpLeosRstpDomainEntry=_WwpLeosRstpDomainEntry_Object((1,3,6,1,4,1,6141,2,60,13,1,1,2,1))
wwpLeosRstpDomainEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:wwpLeosRstpDomainEntry.setStatus(_A)
class _WwpLeosRstpDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRstpDomainId_Type.__name__=_B
_WwpLeosRstpDomainId_Object=MibTableColumn
wwpLeosRstpDomainId=_WwpLeosRstpDomainId_Object((1,3,6,1,4,1,6141,2,60,13,1,1,2,1,1),_WwpLeosRstpDomainId_Type())
wwpLeosRstpDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainId.setStatus(_A)
_WwpLeosRstpDomainName_Type=DisplayString
_WwpLeosRstpDomainName_Object=MibTableColumn
wwpLeosRstpDomainName=_WwpLeosRstpDomainName_Object((1,3,6,1,4,1,6141,2,60,13,1,1,2,1,2),_WwpLeosRstpDomainName_Type())
wwpLeosRstpDomainName.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosRstpDomainName.setStatus(_A)
_WwpLeosRstpDomainStatus_Type=RowStatus
_WwpLeosRstpDomainStatus_Object=MibTableColumn
wwpLeosRstpDomainStatus=_WwpLeosRstpDomainStatus_Object((1,3,6,1,4,1,6141,2,60,13,1,1,2,1,3),_WwpLeosRstpDomainStatus_Type())
wwpLeosRstpDomainStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosRstpDomainStatus.setStatus(_A)
_WwpLeosRstpDomainMemTable_Object=MibTable
wwpLeosRstpDomainMemTable=_WwpLeosRstpDomainMemTable_Object((1,3,6,1,4,1,6141,2,60,13,1,1,3))
if mibBuilder.loadTexts:wwpLeosRstpDomainMemTable.setStatus(_A)
_WwpLeosRstpDomainMemEntry_Object=MibTableRow
wwpLeosRstpDomainMemEntry=_WwpLeosRstpDomainMemEntry_Object((1,3,6,1,4,1,6141,2,60,13,1,1,3,1))
wwpLeosRstpDomainMemEntry.setIndexNames((0,_G,_H),(0,_G,_N))
if mibBuilder.loadTexts:wwpLeosRstpDomainMemEntry.setStatus(_A)
class _WwpLeosRstpDomainPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRstpDomainPortId_Type.__name__=_B
_WwpLeosRstpDomainPortId_Object=MibTableColumn
wwpLeosRstpDomainPortId=_WwpLeosRstpDomainPortId_Object((1,3,6,1,4,1,6141,2,60,13,1,1,3,1,1),_WwpLeosRstpDomainPortId_Type())
wwpLeosRstpDomainPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainPortId.setStatus(_A)
_WwpLeosRstpDomainMemStatus_Type=RowStatus
_WwpLeosRstpDomainMemStatus_Object=MibTableColumn
wwpLeosRstpDomainMemStatus=_WwpLeosRstpDomainMemStatus_Object((1,3,6,1,4,1,6141,2,60,13,1,1,3,1,2),_WwpLeosRstpDomainMemStatus_Type())
wwpLeosRstpDomainMemStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosRstpDomainMemStatus.setStatus(_A)
_WwpLeosRstpBridgeDomainAttrs_ObjectIdentity=ObjectIdentity
wwpLeosRstpBridgeDomainAttrs=_WwpLeosRstpBridgeDomainAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,1,1,4))
class _WwpLeosRstpDomainAttrsForceVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('stp',0),('notDefined',1),('rstp',2)))
_WwpLeosRstpDomainAttrsForceVer_Type.__name__=_B
_WwpLeosRstpDomainAttrsForceVer_Object=MibScalar
wwpLeosRstpDomainAttrsForceVer=_WwpLeosRstpDomainAttrsForceVer_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,1),_WwpLeosRstpDomainAttrsForceVer_Type())
wwpLeosRstpDomainAttrsForceVer.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsForceVer.setStatus(_A)
class _WwpLeosRstpDomainAttrsForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_WwpLeosRstpDomainAttrsForwardDelay_Type.__name__=_B
_WwpLeosRstpDomainAttrsForwardDelay_Object=MibScalar
wwpLeosRstpDomainAttrsForwardDelay=_WwpLeosRstpDomainAttrsForwardDelay_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,2),_WwpLeosRstpDomainAttrsForwardDelay_Type())
wwpLeosRstpDomainAttrsForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsForwardDelay.setStatus(_A)
class _WwpLeosRstpDomainAttrsHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosRstpDomainAttrsHelloTime_Type.__name__=_B
_WwpLeosRstpDomainAttrsHelloTime_Object=MibScalar
wwpLeosRstpDomainAttrsHelloTime=_WwpLeosRstpDomainAttrsHelloTime_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,3),_WwpLeosRstpDomainAttrsHelloTime_Type())
wwpLeosRstpDomainAttrsHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsHelloTime.setStatus(_A)
class _WwpLeosRstpDomainAttrsLoopBackBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_WwpLeosRstpDomainAttrsLoopBackBlock_Type.__name__=_B
_WwpLeosRstpDomainAttrsLoopBackBlock_Object=MibScalar
wwpLeosRstpDomainAttrsLoopBackBlock=_WwpLeosRstpDomainAttrsLoopBackBlock_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,4),_WwpLeosRstpDomainAttrsLoopBackBlock_Type())
wwpLeosRstpDomainAttrsLoopBackBlock.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsLoopBackBlock.setStatus(_A)
class _WwpLeosRstpDomainAttrsMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_WwpLeosRstpDomainAttrsMaxAge_Type.__name__=_B
_WwpLeosRstpDomainAttrsMaxAge_Object=MibScalar
wwpLeosRstpDomainAttrsMaxAge=_WwpLeosRstpDomainAttrsMaxAge_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,5),_WwpLeosRstpDomainAttrsMaxAge_Type())
wwpLeosRstpDomainAttrsMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsMaxAge.setStatus(_A)
class _WwpLeosRstpDomainAttrsPathCostDef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpLeosRstpDomainAttrsPathCostDef_Type.__name__=_B
_WwpLeosRstpDomainAttrsPathCostDef_Object=MibScalar
wwpLeosRstpDomainAttrsPathCostDef=_WwpLeosRstpDomainAttrsPathCostDef_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,6),_WwpLeosRstpDomainAttrsPathCostDef_Type())
wwpLeosRstpDomainAttrsPathCostDef.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsPathCostDef.setStatus(_A)
class _WwpLeosRstpDomainAttrsPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosRstpDomainAttrsPriority_Type.__name__=_B
_WwpLeosRstpDomainAttrsPriority_Object=MibScalar
wwpLeosRstpDomainAttrsPriority=_WwpLeosRstpDomainAttrsPriority_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,7),_WwpLeosRstpDomainAttrsPriority_Type())
wwpLeosRstpDomainAttrsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsPriority.setStatus(_A)
class _WwpLeosRstpDomainAttrsTxHoldCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosRstpDomainAttrsTxHoldCount_Type.__name__=_B
_WwpLeosRstpDomainAttrsTxHoldCount_Object=MibScalar
wwpLeosRstpDomainAttrsTxHoldCount=_WwpLeosRstpDomainAttrsTxHoldCount_Object((1,3,6,1,4,1,6141,2,60,13,1,1,4,8),_WwpLeosRstpDomainAttrsTxHoldCount_Type())
wwpLeosRstpDomainAttrsTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrsTxHoldCount.setStatus(_A)
_WwpLeosRstpDomainAttrTable_Object=MibTable
wwpLeosRstpDomainAttrTable=_WwpLeosRstpDomainAttrTable_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5))
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrTable.setStatus(_A)
_WwpLeosRstpDomainAttrEntry_Object=MibTableRow
wwpLeosRstpDomainAttrEntry=_WwpLeosRstpDomainAttrEntry_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1))
wwpLeosRstpDomainAttrEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrEntry.setStatus(_A)
class _WwpLeosRstpDomainAttrDesignatedBridgePri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRstpDomainAttrDesignatedBridgePri_Type.__name__=_B
_WwpLeosRstpDomainAttrDesignatedBridgePri_Object=MibTableColumn
wwpLeosRstpDomainAttrDesignatedBridgePri=_WwpLeosRstpDomainAttrDesignatedBridgePri_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,1),_WwpLeosRstpDomainAttrDesignatedBridgePri_Type())
wwpLeosRstpDomainAttrDesignatedBridgePri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrDesignatedBridgePri.setStatus(_A)
_WwpLeosRstpDomainAttrDesignatedBridgeMac_Type=MacAddress
_WwpLeosRstpDomainAttrDesignatedBridgeMac_Object=MibTableColumn
wwpLeosRstpDomainAttrDesignatedBridgeMac=_WwpLeosRstpDomainAttrDesignatedBridgeMac_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,2),_WwpLeosRstpDomainAttrDesignatedBridgeMac_Type())
wwpLeosRstpDomainAttrDesignatedBridgeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrDesignatedBridgeMac.setStatus(_A)
class _WwpLeosRstpDomainAttrDesignatedRootPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRstpDomainAttrDesignatedRootPri_Type.__name__=_B
_WwpLeosRstpDomainAttrDesignatedRootPri_Object=MibTableColumn
wwpLeosRstpDomainAttrDesignatedRootPri=_WwpLeosRstpDomainAttrDesignatedRootPri_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,3),_WwpLeosRstpDomainAttrDesignatedRootPri_Type())
wwpLeosRstpDomainAttrDesignatedRootPri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrDesignatedRootPri.setStatus(_A)
_WwpLeosRstpDomainAttrDesignatedRootMac_Type=MacAddress
_WwpLeosRstpDomainAttrDesignatedRootMac_Object=MibTableColumn
wwpLeosRstpDomainAttrDesignatedRootMac=_WwpLeosRstpDomainAttrDesignatedRootMac_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,4),_WwpLeosRstpDomainAttrDesignatedRootMac_Type())
wwpLeosRstpDomainAttrDesignatedRootMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrDesignatedRootMac.setStatus(_A)
class _WwpLeosRstpDomainAttrRootCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRstpDomainAttrRootCost_Type.__name__=_B
_WwpLeosRstpDomainAttrRootCost_Object=MibTableColumn
wwpLeosRstpDomainAttrRootCost=_WwpLeosRstpDomainAttrRootCost_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,5),_WwpLeosRstpDomainAttrRootCost_Type())
wwpLeosRstpDomainAttrRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrRootCost.setStatus(_A)
class _WwpLeosRstpDomainAttrRootPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRstpDomainAttrRootPort_Type.__name__=_B
_WwpLeosRstpDomainAttrRootPort_Object=MibTableColumn
wwpLeosRstpDomainAttrRootPort=_WwpLeosRstpDomainAttrRootPort_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,6),_WwpLeosRstpDomainAttrRootPort_Type())
wwpLeosRstpDomainAttrRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrRootPort.setStatus(_A)
class _WwpLeosRstpDomainAttrMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_WwpLeosRstpDomainAttrMaxAge_Type.__name__=_B
_WwpLeosRstpDomainAttrMaxAge_Object=MibTableColumn
wwpLeosRstpDomainAttrMaxAge=_WwpLeosRstpDomainAttrMaxAge_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,7),_WwpLeosRstpDomainAttrMaxAge_Type())
wwpLeosRstpDomainAttrMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrMaxAge.setStatus(_A)
class _WwpLeosRstpDomainAttrHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosRstpDomainAttrHelloTime_Type.__name__=_B
_WwpLeosRstpDomainAttrHelloTime_Object=MibTableColumn
wwpLeosRstpDomainAttrHelloTime=_WwpLeosRstpDomainAttrHelloTime_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,8),_WwpLeosRstpDomainAttrHelloTime_Type())
wwpLeosRstpDomainAttrHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrHelloTime.setStatus(_A)
class _WwpLeosRstpDomainAttrHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRstpDomainAttrHoldTime_Type.__name__=_B
_WwpLeosRstpDomainAttrHoldTime_Object=MibTableColumn
wwpLeosRstpDomainAttrHoldTime=_WwpLeosRstpDomainAttrHoldTime_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,9),_WwpLeosRstpDomainAttrHoldTime_Type())
wwpLeosRstpDomainAttrHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrHoldTime.setStatus(_A)
class _WwpLeosRstpDomainAttrForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_WwpLeosRstpDomainAttrForwardDelay_Type.__name__=_B
_WwpLeosRstpDomainAttrForwardDelay_Object=MibTableColumn
wwpLeosRstpDomainAttrForwardDelay=_WwpLeosRstpDomainAttrForwardDelay_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,10),_WwpLeosRstpDomainAttrForwardDelay_Type())
wwpLeosRstpDomainAttrForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrForwardDelay.setStatus(_A)
class _WwpLeosRstpDomainAttrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosRstpDomainAttrPriority_Type.__name__=_B
_WwpLeosRstpDomainAttrPriority_Object=MibTableColumn
wwpLeosRstpDomainAttrPriority=_WwpLeosRstpDomainAttrPriority_Object((1,3,6,1,4,1,6141,2,60,13,1,1,5,1,11),_WwpLeosRstpDomainAttrPriority_Type())
wwpLeosRstpDomainAttrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpDomainAttrPriority.setStatus(_A)
class _WwpLeosRstpMaxAgeEventInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_WwpLeosRstpMaxAgeEventInterval_Type.__name__=_B
_WwpLeosRstpMaxAgeEventInterval_Object=MibScalar
wwpLeosRstpMaxAgeEventInterval=_WwpLeosRstpMaxAgeEventInterval_Object((1,3,6,1,4,1,6141,2,60,13,1,1,6),_WwpLeosRstpMaxAgeEventInterval_Type())
wwpLeosRstpMaxAgeEventInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpMaxAgeEventInterval.setStatus(_A)
_WwpLeosRstpPortExt_ObjectIdentity=ObjectIdentity
wwpLeosRstpPortExt=_WwpLeosRstpPortExt_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,1,2))
_WwpLeosRstpPortInfoTable_Object=MibTable
wwpLeosRstpPortInfoTable=_WwpLeosRstpPortInfoTable_Object((1,3,6,1,4,1,6141,2,60,13,1,2,1))
if mibBuilder.loadTexts:wwpLeosRstpPortInfoTable.setStatus(_A)
_WwpLeosRstpPortInfoEntry_Object=MibTableRow
wwpLeosRstpPortInfoEntry=_WwpLeosRstpPortInfoEntry_Object((1,3,6,1,4,1,6141,2,60,13,1,2,1,1))
wwpLeosRstpPortInfoEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:wwpLeosRstpPortInfoEntry.setStatus(_A)
class _WwpLeosRstpPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRstpPortId_Type.__name__=_B
_WwpLeosRstpPortId_Object=MibTableColumn
wwpLeosRstpPortId=_WwpLeosRstpPortId_Object((1,3,6,1,4,1,6141,2,60,13,1,2,1,1,1),_WwpLeosRstpPortId_Type())
wwpLeosRstpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpPortId.setStatus(_A)
_WwpLeosRstpPortDesiginatedId_Type=MacAddress
_WwpLeosRstpPortDesiginatedId_Object=MibTableColumn
wwpLeosRstpPortDesiginatedId=_WwpLeosRstpPortDesiginatedId_Object((1,3,6,1,4,1,6141,2,60,13,1,2,1,1,2),_WwpLeosRstpPortDesiginatedId_Type())
wwpLeosRstpPortDesiginatedId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpPortDesiginatedId.setStatus(_A)
class _WwpLeosRstpPortDesiginatedPid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WwpLeosRstpPortDesiginatedPid_Type.__name__=_K
_WwpLeosRstpPortDesiginatedPid_Object=MibTableColumn
wwpLeosRstpPortDesiginatedPid=_WwpLeosRstpPortDesiginatedPid_Object((1,3,6,1,4,1,6141,2,60,13,1,2,1,1,3),_WwpLeosRstpPortDesiginatedPid_Type())
wwpLeosRstpPortDesiginatedPid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRstpPortDesiginatedPid.setStatus(_A)
_WwpLeosRstpLocalPortExt_ObjectIdentity=ObjectIdentity
wwpLeosRstpLocalPortExt=_WwpLeosRstpLocalPortExt_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,1,3))
_WwpLeosRstpLocalPortInfoTable_Object=MibTable
wwpLeosRstpLocalPortInfoTable=_WwpLeosRstpLocalPortInfoTable_Object((1,3,6,1,4,1,6141,2,60,13,1,3,1))
if mibBuilder.loadTexts:wwpLeosRstpLocalPortInfoTable.setStatus(_A)
_WwpLeosRstpLocalPortInfoEntry_Object=MibTableRow
wwpLeosRstpLocalPortInfoEntry=_WwpLeosRstpLocalPortInfoEntry_Object((1,3,6,1,4,1,6141,2,60,13,1,3,1,1))
wwpLeosRstpLocalPortInfoEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:wwpLeosRstpLocalPortInfoEntry.setStatus(_A)
class _WwpLeosRstpPortDynPathCostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_WwpLeosRstpPortDynPathCostState_Type.__name__=_B
_WwpLeosRstpPortDynPathCostState_Object=MibTableColumn
wwpLeosRstpPortDynPathCostState=_WwpLeosRstpPortDynPathCostState_Object((1,3,6,1,4,1,6141,2,60,13,1,3,1,1,1),_WwpLeosRstpPortDynPathCostState_Type())
wwpLeosRstpPortDynPathCostState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRstpPortDynPathCostState.setStatus(_A)
_WwpLeosRstpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBNotificationPrefix=_WwpLeosRstpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,2))
_WwpLeosRstpMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBNotifications=_WwpLeosRstpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,2,0))
_WwpLeosRstpMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBConformance=_WwpLeosRstpMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,3))
_WwpLeosRstpMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBCompliances=_WwpLeosRstpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,3,1))
_WwpLeosRstpMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosRstpMIBGroups=_WwpLeosRstpMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,13,3,2))
wwpLeosRstpPortBackupNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,1))
wwpLeosRstpPortBackupNotification.setObjects((_E,_F))
if mibBuilder.loadTexts:wwpLeosRstpPortBackupNotification.setStatus(_A)
wwpLeosRstpPvstBpduReceivedNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,2))
wwpLeosRstpPvstBpduReceivedNotification.setObjects((_E,_F))
if mibBuilder.loadTexts:wwpLeosRstpPvstBpduReceivedNotification.setStatus('deprecated')
wwpLeosRstpSelfLoopNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,3))
wwpLeosRstpSelfLoopNotification.setObjects((_E,_F))
if mibBuilder.loadTexts:wwpLeosRstpSelfLoopNotification.setStatus(_A)
wwpLeosRstpPortOperEdgeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,4))
wwpLeosRstpPortOperEdgeNotification.setObjects(*((_E,_F),(_L,_M)))
if mibBuilder.loadTexts:wwpLeosRstpPortOperEdgeNotification.setStatus(_A)
wwpLeosRstpPortFlapNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,5))
wwpLeosRstpPortFlapNotification.setObjects((_E,_F))
if mibBuilder.loadTexts:wwpLeosRstpPortFlapNotification.setStatus(_A)
wwpLeosRstpBridgeRootPortLostNotification=NotificationType((1,3,6,1,4,1,6141,2,60,13,2,0,6))
wwpLeosRstpBridgeRootPortLostNotification.setObjects((_E,_F))
if mibBuilder.loadTexts:wwpLeosRstpBridgeRootPortLostNotification.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'wwpLeosRstpMIB':wwpLeosRstpMIB,'wwpLeosRstpMIBObjects':wwpLeosRstpMIBObjects,'wwpLeosRstpDomain':wwpLeosRstpDomain,'wwpLeosRstpMode':wwpLeosRstpMode,'wwpLeosRstpDomainTable':wwpLeosRstpDomainTable,'wwpLeosRstpDomainEntry':wwpLeosRstpDomainEntry,_H:wwpLeosRstpDomainId,'wwpLeosRstpDomainName':wwpLeosRstpDomainName,'wwpLeosRstpDomainStatus':wwpLeosRstpDomainStatus,'wwpLeosRstpDomainMemTable':wwpLeosRstpDomainMemTable,'wwpLeosRstpDomainMemEntry':wwpLeosRstpDomainMemEntry,_N:wwpLeosRstpDomainPortId,'wwpLeosRstpDomainMemStatus':wwpLeosRstpDomainMemStatus,'wwpLeosRstpBridgeDomainAttrs':wwpLeosRstpBridgeDomainAttrs,'wwpLeosRstpDomainAttrsForceVer':wwpLeosRstpDomainAttrsForceVer,'wwpLeosRstpDomainAttrsForwardDelay':wwpLeosRstpDomainAttrsForwardDelay,'wwpLeosRstpDomainAttrsHelloTime':wwpLeosRstpDomainAttrsHelloTime,'wwpLeosRstpDomainAttrsLoopBackBlock':wwpLeosRstpDomainAttrsLoopBackBlock,'wwpLeosRstpDomainAttrsMaxAge':wwpLeosRstpDomainAttrsMaxAge,'wwpLeosRstpDomainAttrsPathCostDef':wwpLeosRstpDomainAttrsPathCostDef,'wwpLeosRstpDomainAttrsPriority':wwpLeosRstpDomainAttrsPriority,'wwpLeosRstpDomainAttrsTxHoldCount':wwpLeosRstpDomainAttrsTxHoldCount,'wwpLeosRstpDomainAttrTable':wwpLeosRstpDomainAttrTable,'wwpLeosRstpDomainAttrEntry':wwpLeosRstpDomainAttrEntry,'wwpLeosRstpDomainAttrDesignatedBridgePri':wwpLeosRstpDomainAttrDesignatedBridgePri,'wwpLeosRstpDomainAttrDesignatedBridgeMac':wwpLeosRstpDomainAttrDesignatedBridgeMac,'wwpLeosRstpDomainAttrDesignatedRootPri':wwpLeosRstpDomainAttrDesignatedRootPri,'wwpLeosRstpDomainAttrDesignatedRootMac':wwpLeosRstpDomainAttrDesignatedRootMac,'wwpLeosRstpDomainAttrRootCost':wwpLeosRstpDomainAttrRootCost,'wwpLeosRstpDomainAttrRootPort':wwpLeosRstpDomainAttrRootPort,'wwpLeosRstpDomainAttrMaxAge':wwpLeosRstpDomainAttrMaxAge,'wwpLeosRstpDomainAttrHelloTime':wwpLeosRstpDomainAttrHelloTime,'wwpLeosRstpDomainAttrHoldTime':wwpLeosRstpDomainAttrHoldTime,'wwpLeosRstpDomainAttrForwardDelay':wwpLeosRstpDomainAttrForwardDelay,'wwpLeosRstpDomainAttrPriority':wwpLeosRstpDomainAttrPriority,'wwpLeosRstpMaxAgeEventInterval':wwpLeosRstpMaxAgeEventInterval,'wwpLeosRstpPortExt':wwpLeosRstpPortExt,'wwpLeosRstpPortInfoTable':wwpLeosRstpPortInfoTable,'wwpLeosRstpPortInfoEntry':wwpLeosRstpPortInfoEntry,_J:wwpLeosRstpPortId,'wwpLeosRstpPortDesiginatedId':wwpLeosRstpPortDesiginatedId,'wwpLeosRstpPortDesiginatedPid':wwpLeosRstpPortDesiginatedPid,'wwpLeosRstpLocalPortExt':wwpLeosRstpLocalPortExt,'wwpLeosRstpLocalPortInfoTable':wwpLeosRstpLocalPortInfoTable,'wwpLeosRstpLocalPortInfoEntry':wwpLeosRstpLocalPortInfoEntry,'wwpLeosRstpPortDynPathCostState':wwpLeosRstpPortDynPathCostState,'wwpLeosRstpMIBNotificationPrefix':wwpLeosRstpMIBNotificationPrefix,'wwpLeosRstpMIBNotifications':wwpLeosRstpMIBNotifications,'wwpLeosRstpPortBackupNotification':wwpLeosRstpPortBackupNotification,'wwpLeosRstpPvstBpduReceivedNotification':wwpLeosRstpPvstBpduReceivedNotification,'wwpLeosRstpSelfLoopNotification':wwpLeosRstpSelfLoopNotification,'wwpLeosRstpPortOperEdgeNotification':wwpLeosRstpPortOperEdgeNotification,'wwpLeosRstpPortFlapNotification':wwpLeosRstpPortFlapNotification,'wwpLeosRstpBridgeRootPortLostNotification':wwpLeosRstpBridgeRootPortLostNotification,'wwpLeosRstpMIBConformance':wwpLeosRstpMIBConformance,'wwpLeosRstpMIBCompliances':wwpLeosRstpMIBCompliances,'wwpLeosRstpMIBGroups':wwpLeosRstpMIBGroups})