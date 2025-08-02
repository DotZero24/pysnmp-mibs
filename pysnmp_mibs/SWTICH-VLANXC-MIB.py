_I='read-write'
_H='rcVlanxcVlanIndex'
_G='rcVlanxcInnerVid'
_F='rcVlanxcOuterVid'
_E='read-create'
_D='not-accessible'
_C='SWTICH-VLANXC-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rcVlanxc=ModuleIdentity((1,3,6,1,4,1,8886,6,1,72))
class _RcVlanxcCurrentEntryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RcVlanxcCurrentEntryCount_Type.__name__=_B
_RcVlanxcCurrentEntryCount_Object=MibScalar
rcVlanxcCurrentEntryCount=_RcVlanxcCurrentEntryCount_Object((1,3,6,1,4,1,8886,6,1,72,1),_RcVlanxcCurrentEntryCount_Type())
rcVlanxcCurrentEntryCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:rcVlanxcCurrentEntryCount.setStatus(_A)
_RcVlanxcTable_Object=MibTable
rcVlanxcTable=_RcVlanxcTable_Object((1,3,6,1,4,1,8886,6,1,72,2))
if mibBuilder.loadTexts:rcVlanxcTable.setStatus(_A)
_RcVlanxcEntry_Object=MibTableRow
rcVlanxcEntry=_RcVlanxcEntry_Object((1,3,6,1,4,1,8886,6,1,72,2,1))
rcVlanxcEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rcVlanxcEntry.setStatus(_A)
class _RcVlanxcOuterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanxcOuterVid_Type.__name__=_B
_RcVlanxcOuterVid_Object=MibTableColumn
rcVlanxcOuterVid=_RcVlanxcOuterVid_Object((1,3,6,1,4,1,8886,6,1,72,2,1,1),_RcVlanxcOuterVid_Type())
rcVlanxcOuterVid.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanxcOuterVid.setStatus(_A)
class _RcVlanxcInnerVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(4096,4096))
_RcVlanxcInnerVid_Type.__name__=_B
_RcVlanxcInnerVid_Object=MibTableColumn
rcVlanxcInnerVid=_RcVlanxcInnerVid_Object((1,3,6,1,4,1,8886,6,1,72,2,1,2),_RcVlanxcInnerVid_Type())
rcVlanxcInnerVid.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanxcInnerVid.setStatus(_A)
_RcVlanxcPort1_Type=Integer32
_RcVlanxcPort1_Object=MibTableColumn
rcVlanxcPort1=_RcVlanxcPort1_Object((1,3,6,1,4,1,8886,6,1,72,2,1,3),_RcVlanxcPort1_Type())
rcVlanxcPort1.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanxcPort1.setStatus(_A)
_RcVlanxcPort2_Type=Integer32
_RcVlanxcPort2_Object=MibTableColumn
rcVlanxcPort2=_RcVlanxcPort2_Object((1,3,6,1,4,1,8886,6,1,72,2,1,4),_RcVlanxcPort2_Type())
rcVlanxcPort2.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanxcPort2.setStatus(_A)
_RcVlanxcRowStatus_Type=RowStatus
_RcVlanxcRowStatus_Object=MibTableColumn
rcVlanxcRowStatus=_RcVlanxcRowStatus_Object((1,3,6,1,4,1,8886,6,1,72,2,1,5),_RcVlanxcRowStatus_Type())
rcVlanxcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanxcRowStatus.setStatus(_A)
_RcVlanxcVlanTable_Object=MibTable
rcVlanxcVlanTable=_RcVlanxcVlanTable_Object((1,3,6,1,4,1,8886,6,1,72,3))
if mibBuilder.loadTexts:rcVlanxcVlanTable.setStatus(_A)
_RcVlanxcVlanEntry_Object=MibTableRow
rcVlanxcVlanEntry=_RcVlanxcVlanEntry_Object((1,3,6,1,4,1,8886,6,1,72,3,1))
rcVlanxcVlanEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rcVlanxcVlanEntry.setStatus(_A)
class _RcVlanxcVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanxcVlanIndex_Type.__name__=_B
_RcVlanxcVlanIndex_Object=MibTableColumn
rcVlanxcVlanIndex=_RcVlanxcVlanIndex_Object((1,3,6,1,4,1,8886,6,1,72,3,1,1),_RcVlanxcVlanIndex_Type())
rcVlanxcVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanxcVlanIndex.setStatus(_A)
class _RcVlanxcVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bridge',0),('vlan-xc',1),('extend-vlan-xc',2)))
_RcVlanxcVlanMode_Type.__name__=_B
_RcVlanxcVlanMode_Object=MibTableColumn
rcVlanxcVlanMode=_RcVlanxcVlanMode_Object((1,3,6,1,4,1,8886,6,1,72,3,1,2),_RcVlanxcVlanMode_Type())
rcVlanxcVlanMode.setMaxAccess(_I)
if mibBuilder.loadTexts:rcVlanxcVlanMode.setStatus(_A)
_RcVlanxcVlanRowStatus_Type=RowStatus
_RcVlanxcVlanRowStatus_Object=MibTableColumn
rcVlanxcVlanRowStatus=_RcVlanxcVlanRowStatus_Object((1,3,6,1,4,1,8886,6,1,72,3,1,3),_RcVlanxcVlanRowStatus_Type())
rcVlanxcVlanRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:rcVlanxcVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcVlanxc':rcVlanxc,'rcVlanxcCurrentEntryCount':rcVlanxcCurrentEntryCount,'rcVlanxcTable':rcVlanxcTable,'rcVlanxcEntry':rcVlanxcEntry,_F:rcVlanxcOuterVid,_G:rcVlanxcInnerVid,'rcVlanxcPort1':rcVlanxcPort1,'rcVlanxcPort2':rcVlanxcPort2,'rcVlanxcRowStatus':rcVlanxcRowStatus,'rcVlanxcVlanTable':rcVlanxcVlanTable,'rcVlanxcVlanEntry':rcVlanxcVlanEntry,_H:rcVlanxcVlanIndex,'rcVlanxcVlanMode':rcVlanxcVlanMode,'rcVlanxcVlanRowStatus':rcVlanxcVlanRowStatus})