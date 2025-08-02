if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSPVTG=ModuleIdentity((1,3,6,1,4,1,1429))
if mibBuilder.loadTexts:ciscoSPVTG.setRevisions(('2010-08-30 11:00','2009-11-26 15:00'))
_CiscoSat_ObjectIdentity=ObjectIdentity
ciscoSat=_CiscoSat_ObjectIdentity((1,3,6,1,4,1,1429,2))
_CiscoDMN_ObjectIdentity=ObjectIdentity
ciscoDMN=_CiscoDMN_ObjectIdentity((1,3,6,1,4,1,1429,2,2))
_CiscoDSGUtilities_ObjectIdentity=ObjectIdentity
ciscoDSGUtilities=_CiscoDSGUtilities_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5))
_CiscoDSGProducts_ObjectIdentity=ObjectIdentity
ciscoDSGProducts=_CiscoDSGProducts_ObjectIdentity((1,3,6,1,4,1,1429,2,2,6))
mibBuilder.exportSymbols('CISCO-DMN-DSG-ROOT-MIB',**{'ciscoSPVTG':ciscoSPVTG,'ciscoSat':ciscoSat,'ciscoDMN':ciscoDMN,'ciscoDSGUtilities':ciscoDSGUtilities,'ciscoDSGProducts':ciscoDSGProducts})