_E='read-create'
_D='llc2IfIndex'
_C='MAIPU-LLC2-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpLlc2Mib=ModuleIdentity((1,3,6,1,4,1,5651,3,23))
_Llc2ConfTable_Object=MibTable
llc2ConfTable=_Llc2ConfTable_Object((1,3,6,1,4,1,5651,3,23,1))
if mibBuilder.loadTexts:llc2ConfTable.setStatus(_A)
_Llc2ConfEntry_Object=MibTableRow
llc2ConfEntry=_Llc2ConfEntry_Object((1,3,6,1,4,1,5651,3,23,1,1))
llc2ConfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:llc2ConfEntry.setStatus(_A)
_Llc2IfIndex_Type=Integer32
_Llc2IfIndex_Object=MibTableColumn
llc2IfIndex=_Llc2IfIndex_Object((1,3,6,1,4,1,5651,3,23,1,1,1),_Llc2IfIndex_Type())
llc2IfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:llc2IfIndex.setStatus(_A)
class _Llc2Group_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Llc2Group_Type.__name__=_B
_Llc2Group_Object=MibTableColumn
llc2Group=_Llc2Group_Object((1,3,6,1,4,1,5651,3,23,1,1,2),_Llc2Group_Type())
llc2Group.setMaxAccess(_E)
if mibBuilder.loadTexts:llc2Group.setStatus(_A)
_Llc2Status_Type=RowStatus
_Llc2Status_Object=MibTableColumn
llc2Status=_Llc2Status_Object((1,3,6,1,4,1,5651,3,23,1,1,3),_Llc2Status_Type())
llc2Status.setMaxAccess(_E)
if mibBuilder.loadTexts:llc2Status.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mpLlc2Mib':mpLlc2Mib,'llc2ConfTable':llc2ConfTable,'llc2ConfEntry':llc2ConfEntry,_D:llc2IfIndex,'llc2Group':llc2Group,'llc2Status':llc2Status})