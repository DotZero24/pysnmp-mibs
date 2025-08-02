_E='read-write'
_D='vrVrId'
_C='OCNOS-VR-MIB'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
vr=ModuleIdentity((1,3,6,1,4,1,36673,2))
if mibBuilder.loadTexts:vr.setRevisions(('2018-06-21 00:00',))
_VrVrTable_Object=MibTable
vrVrTable=_VrVrTable_Object((1,3,6,1,4,1,36673,2,1))
if mibBuilder.loadTexts:vrVrTable.setStatus(_A)
_VrVrEntry_Object=MibTableRow
vrVrEntry=_VrVrEntry_Object((1,3,6,1,4,1,36673,2,1,1))
vrVrEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:vrVrEntry.setStatus(_A)
class _VrVrId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrVrId_Type.__name__=_B
_VrVrId_Object=MibTableColumn
vrVrId=_VrVrId_Object((1,3,6,1,4,1,36673,2,1,1,1),_VrVrId_Type())
vrVrId.setMaxAccess(_E)
if mibBuilder.loadTexts:vrVrId.setStatus(_A)
_VrName_Type=OctetString
_VrName_Object=MibTableColumn
vrName=_VrName_Object((1,3,6,1,4,1,36673,2,1,1,2),_VrName_Type())
vrName.setMaxAccess(_E)
if mibBuilder.loadTexts:vrName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'vr':vr,'vrVrTable':vrVrTable,'vrVrEntry':vrVrEntry,_D:vrVrId,'vrName':vrName})