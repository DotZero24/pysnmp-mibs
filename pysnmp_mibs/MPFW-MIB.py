_G='fwIfDirection'
_F='fwIfName'
_E='Integer32'
_D='read-create'
_C='MPFW-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_B,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpFwMib=ModuleIdentity((1,3,6,1,4,1,5651,3,35))
_MpFwIfTable_Object=MibTable
mpFwIfTable=_MpFwIfTable_Object((1,3,6,1,4,1,5651,3,35,10))
if mibBuilder.loadTexts:mpFwIfTable.setStatus(_A)
_MpFwIfEntry_Object=MibTableRow
mpFwIfEntry=_MpFwIfEntry_Object((1,3,6,1,4,1,5651,3,35,10,1))
mpFwIfEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:mpFwIfEntry.setStatus(_A)
class _FwIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_FwIfName_Type.__name__=_B
_FwIfName_Object=MibTableColumn
fwIfName=_FwIfName_Object((1,3,6,1,4,1,5651,3,35,10,1,1),_FwIfName_Type())
fwIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:fwIfName.setStatus(_A)
class _FwIfDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_FwIfDirection_Type.__name__=_E
_FwIfDirection_Object=MibTableColumn
fwIfDirection=_FwIfDirection_Object((1,3,6,1,4,1,5651,3,35,10,1,2),_FwIfDirection_Type())
fwIfDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:fwIfDirection.setStatus(_A)
class _FwIfGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FwIfGrpName_Type.__name__=_B
_FwIfGrpName_Object=MibTableColumn
fwIfGrpName=_FwIfGrpName_Object((1,3,6,1,4,1,5651,3,35,10,1,3),_FwIfGrpName_Type())
fwIfGrpName.setMaxAccess('read-write')
if mibBuilder.loadTexts:fwIfGrpName.setStatus(_A)
_FwIfRowStatus_Type=RowStatus
_FwIfRowStatus_Object=MibTableColumn
fwIfRowStatus=_FwIfRowStatus_Object((1,3,6,1,4,1,5651,3,35,10,1,4),_FwIfRowStatus_Type())
fwIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fwIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mpFwMib':mpFwMib,'mpFwIfTable':mpFwIfTable,'mpFwIfEntry':mpFwIfEntry,_F:fwIfName,_G:fwIfDirection,'fwIfGrpName':fwIfGrpName,'fwIfRowStatus':fwIfRowStatus})