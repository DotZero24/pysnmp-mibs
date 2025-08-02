_F='rlCustom1BonjourServiceTypeName'
_E='CISCOSB-1-BONJOUR-SERVICE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlCustom1BonjourService=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,143))
if mibBuilder.loadTexts:rlCustom1BonjourService.setRevisions(('2009-03-24 00:00',))
_RlCustom1BonjourServiceTable_Object=MibTable
rlCustom1BonjourServiceTable=_RlCustom1BonjourServiceTable_Object((1,3,6,1,4,1,9,6,1,101,143,1))
if mibBuilder.loadTexts:rlCustom1BonjourServiceTable.setStatus(_A)
_RlCustom1BonjourServiceEntry_Object=MibTableRow
rlCustom1BonjourServiceEntry=_RlCustom1BonjourServiceEntry_Object((1,3,6,1,4,1,9,6,1,101,143,1,1))
rlCustom1BonjourServiceEntry.setIndexNames((1,_E,_F))
if mibBuilder.loadTexts:rlCustom1BonjourServiceEntry.setStatus(_A)
class _RlCustom1BonjourServiceTypeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,14))
_RlCustom1BonjourServiceTypeName_Type.__name__=_D
_RlCustom1BonjourServiceTypeName_Object=MibTableColumn
rlCustom1BonjourServiceTypeName=_RlCustom1BonjourServiceTypeName_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,1),_RlCustom1BonjourServiceTypeName_Type())
rlCustom1BonjourServiceTypeName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlCustom1BonjourServiceTypeName.setStatus(_A)
class _RlCustom1BonjourServiceTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tcp',2)))
_RlCustom1BonjourServiceTransport_Type.__name__=_C
_RlCustom1BonjourServiceTransport_Object=MibTableColumn
rlCustom1BonjourServiceTransport=_RlCustom1BonjourServiceTransport_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,2),_RlCustom1BonjourServiceTransport_Type())
rlCustom1BonjourServiceTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCustom1BonjourServiceTransport.setStatus(_A)
class _RlCustom1BonjourServicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlCustom1BonjourServicePort_Type.__name__=_C
_RlCustom1BonjourServicePort_Object=MibTableColumn
rlCustom1BonjourServicePort=_RlCustom1BonjourServicePort_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,3),_RlCustom1BonjourServicePort_Type())
rlCustom1BonjourServicePort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCustom1BonjourServicePort.setStatus(_A)
_RlCustom1BonjourServiceEnable_Type=TruthValue
_RlCustom1BonjourServiceEnable_Object=MibTableColumn
rlCustom1BonjourServiceEnable=_RlCustom1BonjourServiceEnable_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,4),_RlCustom1BonjourServiceEnable_Type())
rlCustom1BonjourServiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCustom1BonjourServiceEnable.setStatus(_A)
class _RlCustom1BonjourServiceOptions_Type(Bits):namedValues=NamedValues(*(('serviceCanBeDeleted',0),('serviceCanBeDisabled',1),('portCanBeConfigured',2)))
_RlCustom1BonjourServiceOptions_Type.__name__='Bits'
_RlCustom1BonjourServiceOptions_Object=MibTableColumn
rlCustom1BonjourServiceOptions=_RlCustom1BonjourServiceOptions_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,5),_RlCustom1BonjourServiceOptions_Type())
rlCustom1BonjourServiceOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCustom1BonjourServiceOptions.setStatus(_A)
_RlCustom1BonjourServiceStatus_Type=RowStatus
_RlCustom1BonjourServiceStatus_Object=MibTableColumn
rlCustom1BonjourServiceStatus=_RlCustom1BonjourServiceStatus_Object((1,3,6,1,4,1,9,6,1,101,143,1,1,6),_RlCustom1BonjourServiceStatus_Type())
rlCustom1BonjourServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCustom1BonjourServiceStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlCustom1BonjourService':rlCustom1BonjourService,'rlCustom1BonjourServiceTable':rlCustom1BonjourServiceTable,'rlCustom1BonjourServiceEntry':rlCustom1BonjourServiceEntry,_F:rlCustom1BonjourServiceTypeName,'rlCustom1BonjourServiceTransport':rlCustom1BonjourServiceTransport,'rlCustom1BonjourServicePort':rlCustom1BonjourServicePort,'rlCustom1BonjourServiceEnable':rlCustom1BonjourServiceEnable,'rlCustom1BonjourServiceOptions':rlCustom1BonjourServiceOptions,'rlCustom1BonjourServiceStatus':rlCustom1BonjourServiceStatus})