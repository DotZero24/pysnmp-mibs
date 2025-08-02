_D='read-only'
_C='clientIndex'
_B='EAP-CLIENTTABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clientStatis,=mibBuilder.importSymbols('EAP-CLIENT-MIB','clientStatis')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_ClientTable_Object=MibTable
clientTable=_ClientTable_Object((1,3,6,1,4,1,11863,10,1,1,2))
if mibBuilder.loadTexts:clientTable.setStatus(_A)
_ClientEntry_Object=MibTableRow
clientEntry=_ClientEntry_Object((1,3,6,1,4,1,11863,10,1,1,2,1))
clientEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:clientEntry.setStatus(_A)
_ClientIndex_Type=Integer32
_ClientIndex_Object=MibTableColumn
clientIndex=_ClientIndex_Object((1,3,6,1,4,1,11863,10,1,1,2,1,1),_ClientIndex_Type())
clientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:clientIndex.setStatus(_A)
_MacAddress_Type=OctetString
_MacAddress_Object=MibTableColumn
macAddress=_MacAddress_Object((1,3,6,1,4,1,11863,10,1,1,2,1,2),_MacAddress_Type())
macAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clientTable':clientTable,'clientEntry':clientEntry,_C:clientIndex,'macAddress':macAddress})