_C='rdIndex'
_B='ZHONE-COM-IP-RD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comIpRd=ModuleIdentity((1,3,6,1,4,1,5504,6,53))
if mibBuilder.loadTexts:comIpRd.setRevisions(('2000-09-12 10:02',))
class ZhoneRDIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Rd_ObjectIdentity=ObjectIdentity
rd=_Rd_ObjectIdentity((1,3,6,1,4,1,5504,4,1,3))
if mibBuilder.loadTexts:rd.setStatus(_A)
_RdTable_Object=MibTable
rdTable=_RdTable_Object((1,3,6,1,4,1,5504,4,1,3,1))
if mibBuilder.loadTexts:rdTable.setStatus(_A)
_RdEntry_Object=MibTableRow
rdEntry=_RdEntry_Object((1,3,6,1,4,1,5504,4,1,3,1,1))
rdEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rdEntry.setStatus(_A)
_RdIndex_Type=ZhoneRDIndex
_RdIndex_Object=MibTableColumn
rdIndex=_RdIndex_Object((1,3,6,1,4,1,5504,4,1,3,1,1,1),_RdIndex_Type())
rdIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rdIndex.setStatus(_A)
_RdRowStatus_Type=ZhoneRowStatus
_RdRowStatus_Object=MibTableColumn
rdRowStatus=_RdRowStatus_Object((1,3,6,1,4,1,5504,4,1,3,1,1,2),_RdRowStatus_Type())
rdRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rdRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ZhoneRDIndex':ZhoneRDIndex,'rd':rd,'rdTable':rdTable,'rdEntry':rdEntry,_C:rdIndex,'rdRowStatus':rdRowStatus,'comIpRd':comIpRd})