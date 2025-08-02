_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoRoutePoliciesMIB=ModuleIdentity((1,3,6,1,4,1,9,9,578))
if mibBuilder.loadTexts:ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))
_CiscoRoutePoliciesMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoRoutePoliciesMIBNotifs=_CiscoRoutePoliciesMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,578,0))
_CiscoRoutePoliciesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRoutePoliciesMIBObjects=_CiscoRoutePoliciesMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,578,1))
_CrpPolicies_ObjectIdentity=ObjectIdentity
crpPolicies=_CrpPolicies_ObjectIdentity((1,3,6,1,4,1,9,9,578,1,1))
if mibBuilder.loadTexts:crpPolicies.setStatus(_A)
_CrpPolicyIfIndex_ObjectIdentity=ObjectIdentity
crpPolicyIfIndex=_CrpPolicyIfIndex_ObjectIdentity((1,3,6,1,4,1,9,9,578,1,1,1))
if mibBuilder.loadTexts:crpPolicyIfIndex.setStatus(_A)
_CiscoRoutePoliciesMIBConform_ObjectIdentity=ObjectIdentity
ciscoRoutePoliciesMIBConform=_CiscoRoutePoliciesMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,578,2))
mibBuilder.exportSymbols('CISCO-ROUTE-POLICIES-MIB',**{'ciscoRoutePoliciesMIB':ciscoRoutePoliciesMIB,'ciscoRoutePoliciesMIBNotifs':ciscoRoutePoliciesMIBNotifs,'ciscoRoutePoliciesMIBObjects':ciscoRoutePoliciesMIBObjects,'crpPolicies':crpPolicies,'crpPolicyIfIndex':crpPolicyIfIndex,'ciscoRoutePoliciesMIBConform':ciscoRoutePoliciesMIBConform})