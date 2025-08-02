_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bdcom=ModuleIdentity((1,3,6,1,4,1,3320))
_BdcomProducts_ObjectIdentity=ObjectIdentity
bdcomProducts=_BdcomProducts_ObjectIdentity((1,3,6,1,4,1,3320,1))
if mibBuilder.loadTexts:bdcomProducts.setStatus(_A)
_Bdlocal_ObjectIdentity=ObjectIdentity
bdlocal=_Bdlocal_ObjectIdentity((1,3,6,1,4,1,3320,2))
if mibBuilder.loadTexts:bdlocal.setStatus(_A)
_Bdtemporary_ObjectIdentity=ObjectIdentity
bdtemporary=_Bdtemporary_ObjectIdentity((1,3,6,1,4,1,3320,3))
if mibBuilder.loadTexts:bdtemporary.setStatus(_A)
_BdMgmt_ObjectIdentity=ObjectIdentity
bdMgmt=_BdMgmt_ObjectIdentity((1,3,6,1,4,1,3320,9))
if mibBuilder.loadTexts:bdMgmt.setStatus(_A)
_BdcomModules_ObjectIdentity=ObjectIdentity
bdcomModules=_BdcomModules_ObjectIdentity((1,3,6,1,4,1,3320,12))
if mibBuilder.loadTexts:bdcomModules.setStatus(_A)
_BdcomPolicyAuto_ObjectIdentity=ObjectIdentity
bdcomPolicyAuto=_BdcomPolicyAuto_ObjectIdentity((1,3,6,1,4,1,3320,18))
if mibBuilder.loadTexts:bdcomPolicyAuto.setStatus(_A)
_BdcomPibToMib_ObjectIdentity=ObjectIdentity
bdcomPibToMib=_BdcomPibToMib_ObjectIdentity((1,3,6,1,4,1,3320,18,2))
if mibBuilder.loadTexts:bdcomPibToMib.setStatus(_A)
mibBuilder.exportSymbols('BDCOM-SMI',**{'bdcom':bdcom,'bdcomProducts':bdcomProducts,'bdlocal':bdlocal,'bdtemporary':bdtemporary,'bdMgmt':bdMgmt,'bdcomModules':bdcomModules,'bdcomPolicyAuto':bdcomPolicyAuto,'bdcomPibToMib':bdcomPibToMib})