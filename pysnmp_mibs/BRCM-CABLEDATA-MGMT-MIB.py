if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmt,=mibBuilder.importSymbols('BRCM-CABLEDATA-SMI','cableDataMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cableDataMgmtMIB=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2))
if mibBuilder.loadTexts:cableDataMgmtMIB.setRevisions(('2011-03-01 00:00','2010-08-16 00:00','2009-08-27 00:00','2009-08-26 00:00','2007-02-05 00:00','2002-06-04 00:00'))
_CableDataMgmtMIBObjects_ObjectIdentity=ObjectIdentity
cableDataMgmtMIBObjects=_CableDataMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1))
_CableDataMgmtBase_ObjectIdentity=ObjectIdentity
cableDataMgmtBase=_CableDataMgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,1))
_CableDataMgmtVendor_ObjectIdentity=ObjectIdentity
cableDataMgmtVendor=_CableDataMgmtVendor_ObjectIdentity((1,3,6,1,4,1,4413,2,2,99))
_BroadcomCableDataMgmt_ObjectIdentity=ObjectIdentity
broadcomCableDataMgmt=_BroadcomCableDataMgmt_ObjectIdentity((1,3,6,1,4,1,4413,2,2,99,4413))
mibBuilder.exportSymbols('BRCM-CABLEDATA-MGMT-MIB',**{'cableDataMgmtMIB':cableDataMgmtMIB,'cableDataMgmtMIBObjects':cableDataMgmtMIBObjects,'cableDataMgmtBase':cableDataMgmtBase,'cableDataMgmtVendor':cableDataMgmtVendor,'broadcomCableDataMgmt':broadcomCableDataMgmt})