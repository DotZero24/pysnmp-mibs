_E='hpnicflldpPortConfigPortNum'
_D='HPN-ICF-LLDP-EXT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
LldpPortNumber,=mibBuilder.importSymbols('LLDP-MIB','LldpPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicflldp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,100))
if mibBuilder.loadTexts:hpnicflldp.setRevisions(('2009-03-21 00:00',))
_HpnicflldpObjects_ObjectIdentity=ObjectIdentity
hpnicflldpObjects=_HpnicflldpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,100,1))
_HpnicflldpConfiguration_ObjectIdentity=ObjectIdentity
hpnicflldpConfiguration=_HpnicflldpConfiguration_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1))
_HpnicflldpAdminStatus_Type=TruthValue
_HpnicflldpAdminStatus_Object=MibScalar
hpnicflldpAdminStatus=_HpnicflldpAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,1),_HpnicflldpAdminStatus_Type())
hpnicflldpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicflldpAdminStatus.setStatus(_A)
_HpnicflldpComplianceCDPStatus_Type=TruthValue
_HpnicflldpComplianceCDPStatus_Object=MibScalar
hpnicflldpComplianceCDPStatus=_HpnicflldpComplianceCDPStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,2),_HpnicflldpComplianceCDPStatus_Type())
hpnicflldpComplianceCDPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicflldpComplianceCDPStatus.setStatus(_A)
_HpnicflldpPortConfigTable_Object=MibTable
hpnicflldpPortConfigTable=_HpnicflldpPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,3))
if mibBuilder.loadTexts:hpnicflldpPortConfigTable.setStatus(_A)
_HpnicflldpPortConfigEntry_Object=MibTableRow
hpnicflldpPortConfigEntry=_HpnicflldpPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,3,1))
hpnicflldpPortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicflldpPortConfigEntry.setStatus(_A)
_HpnicflldpPortConfigPortNum_Type=LldpPortNumber
_HpnicflldpPortConfigPortNum_Object=MibTableColumn
hpnicflldpPortConfigPortNum=_HpnicflldpPortConfigPortNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,3,1,1),_HpnicflldpPortConfigPortNum_Type())
hpnicflldpPortConfigPortNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicflldpPortConfigPortNum.setStatus(_A)
class _HpnicflldpPortConfigCDPComplianceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('txAndRx',1),('disabled',2)))
_HpnicflldpPortConfigCDPComplianceStatus_Type.__name__=_C
_HpnicflldpPortConfigCDPComplianceStatus_Object=MibTableColumn
hpnicflldpPortConfigCDPComplianceStatus=_HpnicflldpPortConfigCDPComplianceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,100,1,1,3,1,2),_HpnicflldpPortConfigCDPComplianceStatus_Type())
hpnicflldpPortConfigCDPComplianceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicflldpPortConfigCDPComplianceStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicflldp':hpnicflldp,'hpnicflldpObjects':hpnicflldpObjects,'hpnicflldpConfiguration':hpnicflldpConfiguration,'hpnicflldpAdminStatus':hpnicflldpAdminStatus,'hpnicflldpComplianceCDPStatus':hpnicflldpComplianceCDPStatus,'hpnicflldpPortConfigTable':hpnicflldpPortConfigTable,'hpnicflldpPortConfigEntry':hpnicflldpPortConfigEntry,_E:hpnicflldpPortConfigPortNum,'hpnicflldpPortConfigCDPComplianceStatus':hpnicflldpPortConfigCDPComplianceStatus})