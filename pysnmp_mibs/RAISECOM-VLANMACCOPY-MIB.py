_F='rcMacCopyTableIndex'
_E='RAISECOM-VLANMACCOPY-MIB'
_D='rcPortIndex'
_C='SWITCH-SYSTEM-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols(_C,_D)
Vlanset,=mibBuilder.importSymbols('SWITCH-TC','Vlanset')
rcMacConfig=ModuleIdentity((1,3,6,1,4,1,8886,6,1,3))
_RcVlanMacCopyMibObjects_ObjectIdentity=ObjectIdentity
rcVlanMacCopyMibObjects=_RcVlanMacCopyMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,3,5))
_RcVlanMacCopyTable_Object=MibTable
rcVlanMacCopyTable=_RcVlanMacCopyTable_Object((1,3,6,1,4,1,8886,6,1,3,5,1))
if mibBuilder.loadTexts:rcVlanMacCopyTable.setStatus(_A)
_RcVlanMacCopyEntry_Object=MibTableRow
rcVlanMacCopyEntry=_RcVlanMacCopyEntry_Object((1,3,6,1,4,1,8886,6,1,3,5,1,1))
rcVlanMacCopyEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:rcVlanMacCopyEntry.setStatus(_A)
_RcMacCopyTableIndex_Type=Integer32
_RcMacCopyTableIndex_Object=MibTableColumn
rcMacCopyTableIndex=_RcMacCopyTableIndex_Object((1,3,6,1,4,1,8886,6,1,3,5,1,1,1),_RcMacCopyTableIndex_Type())
rcMacCopyTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcMacCopyTableIndex.setStatus(_A)
_RcMacCopyDestVlanList_Type=Vlanset
_RcMacCopyDestVlanList_Object=MibTableColumn
rcMacCopyDestVlanList=_RcMacCopyDestVlanList_Object((1,3,6,1,4,1,8886,6,1,3,5,1,1,2),_RcMacCopyDestVlanList_Type())
rcMacCopyDestVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacCopyDestVlanList.setStatus(_A)
_RcMacCopySourceVlanList_Type=Vlanset
_RcMacCopySourceVlanList_Object=MibTableColumn
rcMacCopySourceVlanList=_RcMacCopySourceVlanList_Object((1,3,6,1,4,1,8886,6,1,3,5,1,1,3),_RcMacCopySourceVlanList_Type())
rcMacCopySourceVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacCopySourceVlanList.setStatus(_A)
_RcMacCopyRowStatus_Type=RowStatus
_RcMacCopyRowStatus_Object=MibTableColumn
rcMacCopyRowStatus=_RcMacCopyRowStatus_Object((1,3,6,1,4,1,8886,6,1,3,5,1,1,4),_RcMacCopyRowStatus_Type())
rcMacCopyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacCopyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcMacConfig':rcMacConfig,'rcVlanMacCopyMibObjects':rcVlanMacCopyMibObjects,'rcVlanMacCopyTable':rcVlanMacCopyTable,'rcVlanMacCopyEntry':rcVlanMacCopyEntry,_F:rcMacCopyTableIndex,'rcMacCopyDestVlanList':rcMacCopyDestVlanList,'rcMacCopySourceVlanList':rcMacCopySourceVlanList,'rcMacCopyRowStatus':rcMacCopyRowStatus})