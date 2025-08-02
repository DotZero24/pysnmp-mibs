_V='wwpMacMgmtSacPortId'
_U='wwpMacMgmtSacVlanID'
_T='wwpMacMgmtCMacIndex'
_S='wwpMacMgmtPMPortId'
_R='wwpMacMgmtPMVlanID'
_Q='static'
_P='dynamic'
_O='wwpMacMgmtMacAddr'
_N='wwpMacMgmtPortId'
_M='wwpMacMgmtVlanID'
_L='wwpMacMgmtCPortId'
_K='wwpMacMgmtCVlanID'
_J='none'
_I='disable'
_H='enable'
_G='TruthValue'
_F='read-create'
_E='read-write'
_D='WWP-MAC-MGMT-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpMacMgmtMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,28))
if mibBuilder.loadTexts:wwpMacMgmtMIB.setRevisions(('2005-11-22 19:00','2003-04-16 00:00','2001-04-03 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpMacMgmtMIBObjects_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBObjects=_WwpMacMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,28,1))
_WwpMacMgmt_ObjectIdentity=ObjectIdentity
wwpMacMgmt=_WwpMacMgmt_ObjectIdentity((1,3,6,1,4,1,6141,2,28,1,1))
_WwpMacMgmtMacTable_Object=MibTable
wwpMacMgmtMacTable=_WwpMacMgmtMacTable_Object((1,3,6,1,4,1,6141,2,28,1,1,1))
if mibBuilder.loadTexts:wwpMacMgmtMacTable.setStatus(_A)
_WwpMacMgmtMacEntry_Object=MibTableRow
wwpMacMgmtMacEntry=_WwpMacMgmtMacEntry_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1))
wwpMacMgmtMacEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:wwpMacMgmtMacEntry.setStatus(_A)
_WwpMacMgmtVlanID_Type=VlanId
_WwpMacMgmtVlanID_Object=MibTableColumn
wwpMacMgmtVlanID=_WwpMacMgmtVlanID_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,1),_WwpMacMgmtVlanID_Type())
wwpMacMgmtVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtVlanID.setStatus(_A)
class _WwpMacMgmtPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpMacMgmtPortId_Type.__name__=_B
_WwpMacMgmtPortId_Object=MibTableColumn
wwpMacMgmtPortId=_WwpMacMgmtPortId_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,2),_WwpMacMgmtPortId_Type())
wwpMacMgmtPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtPortId.setStatus(_A)
_WwpMacMgmtMacAddr_Type=MacAddress
_WwpMacMgmtMacAddr_Object=MibTableColumn
wwpMacMgmtMacAddr=_WwpMacMgmtMacAddr_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,3),_WwpMacMgmtMacAddr_Type())
wwpMacMgmtMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtMacAddr.setStatus(_A)
class _WwpMacMgmtMacAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpMacMgmtMacAddrMode_Type.__name__=_B
_WwpMacMgmtMacAddrMode_Object=MibTableColumn
wwpMacMgmtMacAddrMode=_WwpMacMgmtMacAddrMode_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,4),_WwpMacMgmtMacAddrMode_Type())
wwpMacMgmtMacAddrMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtMacAddrMode.setStatus(_A)
class _WwpMacMgmtMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpMacMgmtMacStatus_Type.__name__=_B
_WwpMacMgmtMacStatus_Object=MibTableColumn
wwpMacMgmtMacStatus=_WwpMacMgmtMacStatus_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,5),_WwpMacMgmtMacStatus_Type())
wwpMacMgmtMacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtMacStatus.setStatus(_A)
_WwpMacMgmtMacRowStatus_Type=RowStatus
_WwpMacMgmtMacRowStatus_Object=MibTableColumn
wwpMacMgmtMacRowStatus=_WwpMacMgmtMacRowStatus_Object((1,3,6,1,4,1,6141,2,28,1,1,1,1,6),_WwpMacMgmtMacRowStatus_Type())
wwpMacMgmtMacRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpMacMgmtMacRowStatus.setStatus(_A)
class _WwpMacMgmtMacReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('reset',1)))
_WwpMacMgmtMacReset_Type.__name__=_B
_WwpMacMgmtMacReset_Object=MibScalar
wwpMacMgmtMacReset=_WwpMacMgmtMacReset_Object((1,3,6,1,4,1,6141,2,28,1,1,2),_WwpMacMgmtMacReset_Type())
wwpMacMgmtMacReset.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtMacReset.setStatus(_A)
_WwpMacMgmtPMTable_Object=MibTable
wwpMacMgmtPMTable=_WwpMacMgmtPMTable_Object((1,3,6,1,4,1,6141,2,28,1,1,3))
if mibBuilder.loadTexts:wwpMacMgmtPMTable.setStatus(_A)
_WwpMacMgmtPMEntry_Object=MibTableRow
wwpMacMgmtPMEntry=_WwpMacMgmtPMEntry_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1))
wwpMacMgmtPMEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:wwpMacMgmtPMEntry.setStatus(_A)
_WwpMacMgmtPMVlanID_Type=VlanId
_WwpMacMgmtPMVlanID_Object=MibTableColumn
wwpMacMgmtPMVlanID=_WwpMacMgmtPMVlanID_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,1),_WwpMacMgmtPMVlanID_Type())
wwpMacMgmtPMVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtPMVlanID.setStatus(_A)
class _WwpMacMgmtPMPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpMacMgmtPMPortId_Type.__name__=_B
_WwpMacMgmtPMPortId_Object=MibTableColumn
wwpMacMgmtPMPortId=_WwpMacMgmtPMPortId_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,2),_WwpMacMgmtPMPortId_Type())
wwpMacMgmtPMPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtPMPortId.setStatus(_A)
class _WwpMacMgmtPMLearnLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_WwpMacMgmtPMLearnLimit_Type.__name__=_B
_WwpMacMgmtPMLearnLimit_Object=MibTableColumn
wwpMacMgmtPMLearnLimit=_WwpMacMgmtPMLearnLimit_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,3),_WwpMacMgmtPMLearnLimit_Type())
wwpMacMgmtPMLearnLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtPMLearnLimit.setStatus(_A)
class _WwpMacMgmtPMLearnCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_WwpMacMgmtPMLearnCount_Type.__name__=_B
_WwpMacMgmtPMLearnCount_Object=MibTableColumn
wwpMacMgmtPMLearnCount=_WwpMacMgmtPMLearnCount_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,4),_WwpMacMgmtPMLearnCount_Type())
wwpMacMgmtPMLearnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtPMLearnCount.setStatus(_A)
class _WwpMacMgmtPMStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpMacMgmtPMStatus_Type.__name__=_B
_WwpMacMgmtPMStatus_Object=MibTableColumn
wwpMacMgmtPMStatus=_WwpMacMgmtPMStatus_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,5),_WwpMacMgmtPMStatus_Type())
wwpMacMgmtPMStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtPMStatus.setStatus(_A)
class _WwpMacMgmtPMMacFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('flush',1)))
_WwpMacMgmtPMMacFlush_Type.__name__=_B
_WwpMacMgmtPMMacFlush_Object=MibTableColumn
wwpMacMgmtPMMacFlush=_WwpMacMgmtPMMacFlush_Object((1,3,6,1,4,1,6141,2,28,1,1,3,1,6),_WwpMacMgmtPMMacFlush_Type())
wwpMacMgmtPMMacFlush.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtPMMacFlush.setStatus(_A)
class _WwpMacMgmtCacheMac_Type(TruthValue):defaultValue=2
_WwpMacMgmtCacheMac_Type.__name__=_G
_WwpMacMgmtCacheMac_Object=MibScalar
wwpMacMgmtCacheMac=_WwpMacMgmtCacheMac_Object((1,3,6,1,4,1,6141,2,28,1,1,4),_WwpMacMgmtCacheMac_Type())
wwpMacMgmtCacheMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpMacMgmtCacheMac.setStatus(_A)
_WwpMacMgmtCacheMacTable_Object=MibTable
wwpMacMgmtCacheMacTable=_WwpMacMgmtCacheMacTable_Object((1,3,6,1,4,1,6141,2,28,1,1,5))
if mibBuilder.loadTexts:wwpMacMgmtCacheMacTable.setStatus(_A)
_WwpMacMgmtCacheMacEntry_Object=MibTableRow
wwpMacMgmtCacheMacEntry=_WwpMacMgmtCacheMacEntry_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1))
wwpMacMgmtCacheMacEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_T))
if mibBuilder.loadTexts:wwpMacMgmtCacheMacEntry.setStatus(_A)
_WwpMacMgmtCVlanID_Type=VlanId
_WwpMacMgmtCVlanID_Object=MibTableColumn
wwpMacMgmtCVlanID=_WwpMacMgmtCVlanID_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,1),_WwpMacMgmtCVlanID_Type())
wwpMacMgmtCVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCVlanID.setStatus(_A)
class _WwpMacMgmtCPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpMacMgmtCPortId_Type.__name__=_B
_WwpMacMgmtCPortId_Object=MibTableColumn
wwpMacMgmtCPortId=_WwpMacMgmtCPortId_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,2),_WwpMacMgmtCPortId_Type())
wwpMacMgmtCPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCPortId.setStatus(_A)
class _WwpMacMgmtCMacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpMacMgmtCMacIndex_Type.__name__=_B
_WwpMacMgmtCMacIndex_Object=MibTableColumn
wwpMacMgmtCMacIndex=_WwpMacMgmtCMacIndex_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,3),_WwpMacMgmtCMacIndex_Type())
wwpMacMgmtCMacIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCMacIndex.setStatus(_A)
_WwpMacMgmtCMacAddr_Type=MacAddress
_WwpMacMgmtCMacAddr_Object=MibTableColumn
wwpMacMgmtCMacAddr=_WwpMacMgmtCMacAddr_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,4),_WwpMacMgmtCMacAddr_Type())
wwpMacMgmtCMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCMacAddr.setStatus(_A)
class _WwpMacMgmtCMacAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpMacMgmtCMacAddrMode_Type.__name__=_B
_WwpMacMgmtCMacAddrMode_Object=MibTableColumn
wwpMacMgmtCMacAddrMode=_WwpMacMgmtCMacAddrMode_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,5),_WwpMacMgmtCMacAddrMode_Type())
wwpMacMgmtCMacAddrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCMacAddrMode.setStatus(_A)
class _WwpMacMgmtCMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpMacMgmtCMacStatus_Type.__name__=_B
_WwpMacMgmtCMacStatus_Object=MibTableColumn
wwpMacMgmtCMacStatus=_WwpMacMgmtCMacStatus_Object((1,3,6,1,4,1,6141,2,28,1,1,5,1,6),_WwpMacMgmtCMacStatus_Type())
wwpMacMgmtCMacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCMacStatus.setStatus(_A)
_WwpMacMgmtCacheMacCountTable_Object=MibTable
wwpMacMgmtCacheMacCountTable=_WwpMacMgmtCacheMacCountTable_Object((1,3,6,1,4,1,6141,2,28,1,1,6))
if mibBuilder.loadTexts:wwpMacMgmtCacheMacCountTable.setStatus(_A)
_WwpMacMgmtCacheMacCountEntry_Object=MibTableRow
wwpMacMgmtCacheMacCountEntry=_WwpMacMgmtCacheMacCountEntry_Object((1,3,6,1,4,1,6141,2,28,1,1,6,1))
wwpMacMgmtCacheMacCountEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:wwpMacMgmtCacheMacCountEntry.setStatus(_A)
class _WwpMacMgmtCacheMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpMacMgmtCacheMacCount_Type.__name__=_B
_WwpMacMgmtCacheMacCount_Object=MibTableColumn
wwpMacMgmtCacheMacCount=_WwpMacMgmtCacheMacCount_Object((1,3,6,1,4,1,6141,2,28,1,1,6,1,1),_WwpMacMgmtCacheMacCount_Type())
wwpMacMgmtCacheMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtCacheMacCount.setStatus(_A)
_WwpMacMgmtSacTable_Object=MibTable
wwpMacMgmtSacTable=_WwpMacMgmtSacTable_Object((1,3,6,1,4,1,6141,2,28,1,1,7))
if mibBuilder.loadTexts:wwpMacMgmtSacTable.setStatus(_A)
_WwpMacMgmtSacEntry_Object=MibTableRow
wwpMacMgmtSacEntry=_WwpMacMgmtSacEntry_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1))
wwpMacMgmtSacEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:wwpMacMgmtSacEntry.setStatus(_A)
_WwpMacMgmtSacVlanID_Type=VlanId
_WwpMacMgmtSacVlanID_Object=MibTableColumn
wwpMacMgmtSacVlanID=_WwpMacMgmtSacVlanID_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,1),_WwpMacMgmtSacVlanID_Type())
wwpMacMgmtSacVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtSacVlanID.setStatus(_A)
class _WwpMacMgmtSacPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpMacMgmtSacPortId_Type.__name__=_B
_WwpMacMgmtSacPortId_Object=MibTableColumn
wwpMacMgmtSacPortId=_WwpMacMgmtSacPortId_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,2),_WwpMacMgmtSacPortId_Type())
wwpMacMgmtSacPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtSacPortId.setStatus(_A)
class _WwpMacMgmtSacLearnCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_WwpMacMgmtSacLearnCount_Type.__name__=_B
_WwpMacMgmtSacLearnCount_Object=MibTableColumn
wwpMacMgmtSacLearnCount=_WwpMacMgmtSacLearnCount_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,3),_WwpMacMgmtSacLearnCount_Type())
wwpMacMgmtSacLearnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMacMgmtSacLearnCount.setStatus(_A)
class _WwpMacMgmtSacMaxLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_WwpMacMgmtSacMaxLearn_Type.__name__=_B
_WwpMacMgmtSacMaxLearn_Object=MibTableColumn
wwpMacMgmtSacMaxLearn=_WwpMacMgmtSacMaxLearn_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,4),_WwpMacMgmtSacMaxLearn_Type())
wwpMacMgmtSacMaxLearn.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpMacMgmtSacMaxLearn.setStatus(_A)
class _WwpMacMgmtSacLearnDisabled_Type(TruthValue):defaultValue=2
_WwpMacMgmtSacLearnDisabled_Type.__name__=_G
_WwpMacMgmtSacLearnDisabled_Object=MibTableColumn
wwpMacMgmtSacLearnDisabled=_WwpMacMgmtSacLearnDisabled_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,5),_WwpMacMgmtSacLearnDisabled_Type())
wwpMacMgmtSacLearnDisabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpMacMgmtSacLearnDisabled.setStatus(_A)
class _WwpMacMgmtSacMacFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('flush',1)))
_WwpMacMgmtSacMacFlush_Type.__name__=_B
_WwpMacMgmtSacMacFlush_Object=MibTableColumn
wwpMacMgmtSacMacFlush=_WwpMacMgmtSacMacFlush_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,6),_WwpMacMgmtSacMacFlush_Type())
wwpMacMgmtSacMacFlush.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpMacMgmtSacMacFlush.setStatus(_A)
_WwpMacMgmtSacStatus_Type=RowStatus
_WwpMacMgmtSacStatus_Object=MibTableColumn
wwpMacMgmtSacStatus=_WwpMacMgmtSacStatus_Object((1,3,6,1,4,1,6141,2,28,1,1,7,1,7),_WwpMacMgmtSacStatus_Type())
wwpMacMgmtSacStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpMacMgmtSacStatus.setStatus(_A)
_WwpMacMgmtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBNotificationPrefix=_WwpMacMgmtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,28,2))
_WwpMacMgmtMIBNotifications_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBNotifications=_WwpMacMgmtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,28,2,0))
_WwpMacMgmtMIBConformance_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBConformance=_WwpMacMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,28,3))
_WwpMacMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBCompliances=_WwpMacMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,28,3,1))
_WwpMacMgmtMIBGroups_ObjectIdentity=ObjectIdentity
wwpMacMgmtMIBGroups=_WwpMacMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,28,3,2))
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,'wwpMacMgmtMIB':wwpMacMgmtMIB,'wwpMacMgmtMIBObjects':wwpMacMgmtMIBObjects,'wwpMacMgmt':wwpMacMgmt,'wwpMacMgmtMacTable':wwpMacMgmtMacTable,'wwpMacMgmtMacEntry':wwpMacMgmtMacEntry,_M:wwpMacMgmtVlanID,_N:wwpMacMgmtPortId,_O:wwpMacMgmtMacAddr,'wwpMacMgmtMacAddrMode':wwpMacMgmtMacAddrMode,'wwpMacMgmtMacStatus':wwpMacMgmtMacStatus,'wwpMacMgmtMacRowStatus':wwpMacMgmtMacRowStatus,'wwpMacMgmtMacReset':wwpMacMgmtMacReset,'wwpMacMgmtPMTable':wwpMacMgmtPMTable,'wwpMacMgmtPMEntry':wwpMacMgmtPMEntry,_R:wwpMacMgmtPMVlanID,_S:wwpMacMgmtPMPortId,'wwpMacMgmtPMLearnLimit':wwpMacMgmtPMLearnLimit,'wwpMacMgmtPMLearnCount':wwpMacMgmtPMLearnCount,'wwpMacMgmtPMStatus':wwpMacMgmtPMStatus,'wwpMacMgmtPMMacFlush':wwpMacMgmtPMMacFlush,'wwpMacMgmtCacheMac':wwpMacMgmtCacheMac,'wwpMacMgmtCacheMacTable':wwpMacMgmtCacheMacTable,'wwpMacMgmtCacheMacEntry':wwpMacMgmtCacheMacEntry,_K:wwpMacMgmtCVlanID,_L:wwpMacMgmtCPortId,_T:wwpMacMgmtCMacIndex,'wwpMacMgmtCMacAddr':wwpMacMgmtCMacAddr,'wwpMacMgmtCMacAddrMode':wwpMacMgmtCMacAddrMode,'wwpMacMgmtCMacStatus':wwpMacMgmtCMacStatus,'wwpMacMgmtCacheMacCountTable':wwpMacMgmtCacheMacCountTable,'wwpMacMgmtCacheMacCountEntry':wwpMacMgmtCacheMacCountEntry,'wwpMacMgmtCacheMacCount':wwpMacMgmtCacheMacCount,'wwpMacMgmtSacTable':wwpMacMgmtSacTable,'wwpMacMgmtSacEntry':wwpMacMgmtSacEntry,_U:wwpMacMgmtSacVlanID,_V:wwpMacMgmtSacPortId,'wwpMacMgmtSacLearnCount':wwpMacMgmtSacLearnCount,'wwpMacMgmtSacMaxLearn':wwpMacMgmtSacMaxLearn,'wwpMacMgmtSacLearnDisabled':wwpMacMgmtSacLearnDisabled,'wwpMacMgmtSacMacFlush':wwpMacMgmtSacMacFlush,'wwpMacMgmtSacStatus':wwpMacMgmtSacStatus,'wwpMacMgmtMIBNotificationPrefix':wwpMacMgmtMIBNotificationPrefix,'wwpMacMgmtMIBNotifications':wwpMacMgmtMIBNotifications,'wwpMacMgmtMIBConformance':wwpMacMgmtMIBConformance,'wwpMacMgmtMIBCompliances':wwpMacMgmtMIBCompliances,'wwpMacMgmtMIBGroups':wwpMacMgmtMIBGroups})