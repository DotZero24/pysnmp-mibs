_F='hmITStormControlPktType'
_E='hmITPortId'
_D='HMIT-SW-PORT-STORM-MIB2'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSwPortMIB,hmITSwPortmgrMIB=mibBuilder.importSymbols('HMIT-SW-PORT-MGR-MIB','hmITSwPortMIB','hmITSwPortmgrMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
_HmITStormTable_Object=MibTable
hmITStormTable=_HmITStormTable_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3))
if mibBuilder.loadTexts:hmITStormTable.setStatus(_A)
_HmITStormEntry_Object=MibTableRow
hmITStormEntry=_HmITStormEntry_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1))
hmITStormEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:hmITStormEntry.setStatus(_A)
class _HmITPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HmITPortId_Type.__name__=_B
_HmITPortId_Object=MibTableColumn
hmITPortId=_HmITPortId_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1,1),_HmITPortId_Type())
hmITPortId.setMaxAccess('read-only')
if mibBuilder.loadTexts:hmITPortId.setStatus(_A)
class _HmITStormControlPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('broadcast',2),('multicast',3)))
_HmITStormControlPktType_Type.__name__=_B
_HmITStormControlPktType_Object=MibTableColumn
hmITStormControlPktType=_HmITStormControlPktType_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1,2),_HmITStormControlPktType_Type())
hmITStormControlPktType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITStormControlPktType.setStatus(_A)
class _HmITStormControlLmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('kbps',1),('pps',2),('percent',3),('none',4)))
_HmITStormControlLmtType_Type.__name__=_B
_HmITStormControlLmtType_Object=MibTableColumn
hmITStormControlLmtType=_HmITStormControlLmtType_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1,3),_HmITStormControlLmtType_Type())
hmITStormControlLmtType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITStormControlLmtType.setStatus(_A)
class _HmITStormControlParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HmITStormControlParam_Type.__name__=_B
_HmITStormControlParam_Object=MibTableColumn
hmITStormControlParam=_HmITStormControlParam_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1,4),_HmITStormControlParam_Type())
hmITStormControlParam.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITStormControlParam.setStatus(_A)
_HmITStormRowStatus_Type=RowStatus
_HmITStormRowStatus_Object=MibTableColumn
hmITStormRowStatus=_HmITStormRowStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,3,1,10),_HmITStormRowStatus_Type())
hmITStormRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITStormRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hmITStormTable':hmITStormTable,'hmITStormEntry':hmITStormEntry,_E:hmITPortId,_F:hmITStormControlPktType,'hmITStormControlLmtType':hmITStormControlLmtType,'hmITStormControlParam':hmITStormControlParam,'hmITStormRowStatus':hmITStormRowStatus})