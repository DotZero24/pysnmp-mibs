_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
oacExpIMIp,=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacExpIMIPVrfToIf=ModuleIdentity((1,3,6,1,4,1,13191,10,3,1,11))
class OacExpVrfName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OacExpIMIPVrfToIfTable_Object=MibTable
oacExpIMIPVrfToIfTable=_OacExpIMIPVrfToIfTable_Object((1,3,6,1,4,1,13191,10,3,1,11,1))
if mibBuilder.loadTexts:oacExpIMIPVrfToIfTable.setStatus(_A)
_OacExpIMIPVrfToIfEntry_Object=MibTableRow
oacExpIMIPVrfToIfEntry=_OacExpIMIPVrfToIfEntry_Object((1,3,6,1,4,1,13191,10,3,1,11,1,1))
oacExpIMIPVrfToIfEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:oacExpIMIPVrfToIfEntry.setStatus(_A)
_OacVrfName_Type=OacExpVrfName
_OacVrfName_Object=MibTableColumn
oacVrfName=_OacVrfName_Object((1,3,6,1,4,1,13191,10,3,1,11,1,1,1),_OacVrfName_Type())
oacVrfName.setMaxAccess('read-only')
if mibBuilder.loadTexts:oacVrfName.setStatus(_A)
mibBuilder.exportSymbols('ONEACCESS-VRF-TO-IF-MIB',**{'OacExpVrfName':OacExpVrfName,'oacExpIMIPVrfToIf':oacExpIMIPVrfToIf,'oacExpIMIPVrfToIfTable':oacExpIMIPVrfToIfTable,'oacExpIMIPVrfToIfEntry':oacExpIMIPVrfToIfEntry,'oacVrfName':oacVrfName})