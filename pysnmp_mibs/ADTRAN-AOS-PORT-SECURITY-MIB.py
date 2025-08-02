_B='ifIndex'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSSwitch,=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSSwitch')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ifIndex,ifName=mibBuilder.importSymbols(_A,_B,'ifName')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSPortSecurityID=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,4,1))
_AdGenAOSPortSecurity_ObjectIdentity=ObjectIdentity
adGenAOSPortSecurity=_AdGenAOSPortSecurity_ObjectIdentity((1,3,6,1,4,1,664,5,53,4,1))
_AdGenAOSPortSecurityTraps_ObjectIdentity=ObjectIdentity
adGenAOSPortSecurityTraps=_AdGenAOSPortSecurityTraps_ObjectIdentity((1,3,6,1,4,1,664,5,53,4,1,0))
adGenAOSPortSecurityViolation=NotificationType((1,3,6,1,4,1,664,5,53,4,1,0,0))
adGenAOSPortSecurityViolation.setObjects((_A,_B))
if mibBuilder.loadTexts:adGenAOSPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols('ADTRAN-AOS-PORT-SECURITY-MIB',**{'adGenAOSPortSecurity':adGenAOSPortSecurity,'adGenAOSPortSecurityTraps':adGenAOSPortSecurityTraps,'adGenAOSPortSecurityViolation':adGenAOSPortSecurityViolation,'adGenAOSPortSecurityID':adGenAOSPortSecurityID})