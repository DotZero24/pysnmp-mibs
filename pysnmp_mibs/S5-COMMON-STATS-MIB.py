_O='s5CmNetAddrNetIndx'
_N='s5CmNetAddrMacAddr'
_M='s5CmNetAddrPortIndx'
_L='s5CmNetAddrBrdIndx'
_K='s5CmNetAddrIfIndex'
_J='s5CmFNodeMacAddr'
_I='s5CmFNodeIfIndx'
_H='s5CmSNodeMacAddr'
_G='s5CmSNodePortIndx'
_F='s5CmSNodeBrdIndx'
_E='s5CmSNodeIfIndx'
_D='S5-COMMON-STATS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5Com,=mibBuilder.importSymbols('S5-ROOT-MIB','s5Com')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
_S5CmStat_ObjectIdentity=ObjectIdentity
s5CmStat=_S5CmStat_ObjectIdentity((1,3,6,1,4,1,45,1,6,5,1))
_S5CmSNodeTable_Object=MibTable
s5CmSNodeTable=_S5CmSNodeTable_Object((1,3,6,1,4,1,45,1,6,5,1,1))
if mibBuilder.loadTexts:s5CmSNodeTable.setStatus(_A)
_S5CmSNodeEntry_Object=MibTableRow
s5CmSNodeEntry=_S5CmSNodeEntry_Object((1,3,6,1,4,1,45,1,6,5,1,1,1))
s5CmSNodeEntry.setIndexNames((0,_D,_E),(0,_D,_F),(0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:s5CmSNodeEntry.setStatus(_A)
class _S5CmSNodeIfIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5CmSNodeIfIndx_Type.__name__=_C
_S5CmSNodeIfIndx_Object=MibTableColumn
s5CmSNodeIfIndx=_S5CmSNodeIfIndx_Object((1,3,6,1,4,1,45,1,6,5,1,1,1,1),_S5CmSNodeIfIndx_Type())
s5CmSNodeIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmSNodeIfIndx.setStatus(_A)
class _S5CmSNodeBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5CmSNodeBrdIndx_Type.__name__=_C
_S5CmSNodeBrdIndx_Object=MibTableColumn
s5CmSNodeBrdIndx=_S5CmSNodeBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,1,1,1,2),_S5CmSNodeBrdIndx_Type())
s5CmSNodeBrdIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmSNodeBrdIndx.setStatus(_A)
class _S5CmSNodePortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5CmSNodePortIndx_Type.__name__=_C
_S5CmSNodePortIndx_Object=MibTableColumn
s5CmSNodePortIndx=_S5CmSNodePortIndx_Object((1,3,6,1,4,1,45,1,6,5,1,1,1,3),_S5CmSNodePortIndx_Type())
s5CmSNodePortIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmSNodePortIndx.setStatus(_A)
_S5CmSNodeMacAddr_Type=MacAddress
_S5CmSNodeMacAddr_Object=MibTableColumn
s5CmSNodeMacAddr=_S5CmSNodeMacAddr_Object((1,3,6,1,4,1,45,1,6,5,1,1,1,4),_S5CmSNodeMacAddr_Type())
s5CmSNodeMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmSNodeMacAddr.setStatus(_A)
class _S5CmSNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('active',2),('inactive',3)))
_S5CmSNodeStatus_Type.__name__=_C
_S5CmSNodeStatus_Object=MibTableColumn
s5CmSNodeStatus=_S5CmSNodeStatus_Object((1,3,6,1,4,1,45,1,6,5,1,1,1,5),_S5CmSNodeStatus_Type())
s5CmSNodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmSNodeStatus.setStatus(_A)
_S5CmFNodeTable_Object=MibTable
s5CmFNodeTable=_S5CmFNodeTable_Object((1,3,6,1,4,1,45,1,6,5,1,2))
if mibBuilder.loadTexts:s5CmFNodeTable.setStatus(_A)
_S5CmFNodeEntry_Object=MibTableRow
s5CmFNodeEntry=_S5CmFNodeEntry_Object((1,3,6,1,4,1,45,1,6,5,1,2,1))
s5CmFNodeEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:s5CmFNodeEntry.setStatus(_A)
class _S5CmFNodeIfIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5CmFNodeIfIndx_Type.__name__=_C
_S5CmFNodeIfIndx_Object=MibTableColumn
s5CmFNodeIfIndx=_S5CmFNodeIfIndx_Object((1,3,6,1,4,1,45,1,6,5,1,2,1,1),_S5CmFNodeIfIndx_Type())
s5CmFNodeIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmFNodeIfIndx.setStatus(_A)
_S5CmFNodeMacAddr_Type=MacAddress
_S5CmFNodeMacAddr_Object=MibTableColumn
s5CmFNodeMacAddr=_S5CmFNodeMacAddr_Object((1,3,6,1,4,1,45,1,6,5,1,2,1,2),_S5CmFNodeMacAddr_Type())
s5CmFNodeMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmFNodeMacAddr.setStatus(_A)
class _S5CmFNodeBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5CmFNodeBrdIndx_Type.__name__=_C
_S5CmFNodeBrdIndx_Object=MibTableColumn
s5CmFNodeBrdIndx=_S5CmFNodeBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,1,2,1,3),_S5CmFNodeBrdIndx_Type())
s5CmFNodeBrdIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmFNodeBrdIndx.setStatus(_A)
class _S5CmFNodePortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5CmFNodePortIndx_Type.__name__=_C
_S5CmFNodePortIndx_Object=MibTableColumn
s5CmFNodePortIndx=_S5CmFNodePortIndx_Object((1,3,6,1,4,1,45,1,6,5,1,2,1,4),_S5CmFNodePortIndx_Type())
s5CmFNodePortIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmFNodePortIndx.setStatus(_A)
_S5CmNetAddrTable_Object=MibTable
s5CmNetAddrTable=_S5CmNetAddrTable_Object((1,3,6,1,4,1,45,1,6,5,1,3))
if mibBuilder.loadTexts:s5CmNetAddrTable.setStatus(_A)
_S5CmNetAddrEntry_Object=MibTableRow
s5CmNetAddrEntry=_S5CmNetAddrEntry_Object((1,3,6,1,4,1,45,1,6,5,1,3,1))
s5CmNetAddrEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:s5CmNetAddrEntry.setStatus(_A)
class _S5CmNetAddrIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_S5CmNetAddrIfIndex_Type.__name__=_C
_S5CmNetAddrIfIndex_Object=MibTableColumn
s5CmNetAddrIfIndex=_S5CmNetAddrIfIndex_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,1),_S5CmNetAddrIfIndex_Type())
s5CmNetAddrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrIfIndex.setStatus(_A)
class _S5CmNetAddrBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5CmNetAddrBrdIndx_Type.__name__=_C
_S5CmNetAddrBrdIndx_Object=MibTableColumn
s5CmNetAddrBrdIndx=_S5CmNetAddrBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,2),_S5CmNetAddrBrdIndx_Type())
s5CmNetAddrBrdIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrBrdIndx.setStatus(_A)
class _S5CmNetAddrPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5CmNetAddrPortIndx_Type.__name__=_C
_S5CmNetAddrPortIndx_Object=MibTableColumn
s5CmNetAddrPortIndx=_S5CmNetAddrPortIndx_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,3),_S5CmNetAddrPortIndx_Type())
s5CmNetAddrPortIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrPortIndx.setStatus(_A)
_S5CmNetAddrMacAddr_Type=MacAddress
_S5CmNetAddrMacAddr_Object=MibTableColumn
s5CmNetAddrMacAddr=_S5CmNetAddrMacAddr_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,4),_S5CmNetAddrMacAddr_Type())
s5CmNetAddrMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrMacAddr.setStatus(_A)
class _S5CmNetAddrNetIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5CmNetAddrNetIndx_Type.__name__=_C
_S5CmNetAddrNetIndx_Object=MibTableColumn
s5CmNetAddrNetIndx=_S5CmNetAddrNetIndx_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,5),_S5CmNetAddrNetIndx_Type())
s5CmNetAddrNetIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrNetIndx.setStatus(_A)
class _S5CmNetAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ip',1))
_S5CmNetAddrType_Type.__name__=_C
_S5CmNetAddrType_Object=MibTableColumn
s5CmNetAddrType=_S5CmNetAddrType_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,6),_S5CmNetAddrType_Type())
s5CmNetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrType.setStatus(_A)
_S5CmNetAddrAddr_Type=OctetString
_S5CmNetAddrAddr_Object=MibTableColumn
s5CmNetAddrAddr=_S5CmNetAddrAddr_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,7),_S5CmNetAddrAddr_Type())
s5CmNetAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrAddr.setStatus(_A)
_S5CmNetAddrLastSeen_Type=TimeTicks
_S5CmNetAddrLastSeen_Object=MibTableColumn
s5CmNetAddrLastSeen=_S5CmNetAddrLastSeen_Object((1,3,6,1,4,1,45,1,6,5,1,3,1,8),_S5CmNetAddrLastSeen_Type())
s5CmNetAddrLastSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:s5CmNetAddrLastSeen.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'s5CmStat':s5CmStat,'s5CmSNodeTable':s5CmSNodeTable,'s5CmSNodeEntry':s5CmSNodeEntry,_E:s5CmSNodeIfIndx,_F:s5CmSNodeBrdIndx,_G:s5CmSNodePortIndx,_H:s5CmSNodeMacAddr,'s5CmSNodeStatus':s5CmSNodeStatus,'s5CmFNodeTable':s5CmFNodeTable,'s5CmFNodeEntry':s5CmFNodeEntry,_I:s5CmFNodeIfIndx,_J:s5CmFNodeMacAddr,'s5CmFNodeBrdIndx':s5CmFNodeBrdIndx,'s5CmFNodePortIndx':s5CmFNodePortIndx,'s5CmNetAddrTable':s5CmNetAddrTable,'s5CmNetAddrEntry':s5CmNetAddrEntry,_K:s5CmNetAddrIfIndex,_L:s5CmNetAddrBrdIndx,_M:s5CmNetAddrPortIndx,_N:s5CmNetAddrMacAddr,_O:s5CmNetAddrNetIndx,'s5CmNetAddrType':s5CmNetAddrType,'s5CmNetAddrAddr':s5CmNetAddrAddr,'s5CmNetAddrLastSeen':s5CmNetAddrLastSeen})