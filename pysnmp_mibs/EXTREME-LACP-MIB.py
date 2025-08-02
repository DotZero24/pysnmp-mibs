_E='extremeLacpMemberPort'
_D='extremeLacpGroup'
_C='read-only'
_B='EXTREME-LACP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeLacp=ModuleIdentity((1,3,6,1,4,1,1916,1,19))
class LacpGroupId(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class LacpMemberPort(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ExtremeLacpTable_Object=MibTable
extremeLacpTable=_ExtremeLacpTable_Object((1,3,6,1,4,1,1916,1,19,1))
if mibBuilder.loadTexts:extremeLacpTable.setStatus(_A)
_ExtremeLacpEntry_Object=MibTableRow
extremeLacpEntry=_ExtremeLacpEntry_Object((1,3,6,1,4,1,1916,1,19,1,1))
extremeLacpEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:extremeLacpEntry.setStatus(_A)
_ExtremeLacpGroup_Type=LacpGroupId
_ExtremeLacpGroup_Object=MibTableColumn
extremeLacpGroup=_ExtremeLacpGroup_Object((1,3,6,1,4,1,1916,1,19,1,1,1),_ExtremeLacpGroup_Type())
extremeLacpGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLacpGroup.setStatus(_A)
_ExtremeLacpMemberPort_Type=LacpMemberPort
_ExtremeLacpMemberPort_Object=MibTableColumn
extremeLacpMemberPort=_ExtremeLacpMemberPort_Object((1,3,6,1,4,1,1916,1,19,1,1,2),_ExtremeLacpMemberPort_Type())
extremeLacpMemberPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLacpMemberPort.setStatus(_A)
_ExtremeLacpAggStatus_Type=TruthValue
_ExtremeLacpAggStatus_Object=MibTableColumn
extremeLacpAggStatus=_ExtremeLacpAggStatus_Object((1,3,6,1,4,1,1916,1,19,1,1,3),_ExtremeLacpAggStatus_Type())
extremeLacpAggStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLacpAggStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LacpGroupId':LacpGroupId,'LacpMemberPort':LacpMemberPort,'extremeLacp':extremeLacp,'extremeLacpTable':extremeLacpTable,'extremeLacpEntry':extremeLacpEntry,_D:extremeLacpGroup,_E:extremeLacpMemberPort,'extremeLacpAggStatus':extremeLacpAggStatus})