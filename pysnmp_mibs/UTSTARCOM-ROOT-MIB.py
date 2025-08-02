_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
utstarcom=ModuleIdentity((1,3,6,1,4,1,1949))
if mibBuilder.loadTexts:utstarcom.setRevisions(('2005-09-01 16:21',))
_UtsRoot_ObjectIdentity=ObjectIdentity
utsRoot=_UtsRoot_ObjectIdentity((1,3,6,1,4,1,1949,1))
_UtsProducts_ObjectIdentity=ObjectIdentity
utsProducts=_UtsProducts_ObjectIdentity((1,3,6,1,4,1,1949,1,3))
_UtsBroadbandSwitch_ObjectIdentity=ObjectIdentity
utsBroadbandSwitch=_UtsBroadbandSwitch_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10))
_UtsBBSProductSysId_ObjectIdentity=ObjectIdentity
utsBBSProductSysId=_UtsBBSProductSysId_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,2))
_UtBBSEponOnuSysId_ObjectIdentity=ObjectIdentity
utBBSEponOnuSysId=_UtBBSEponOnuSysId_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,2,100))
_UtBBSEponOnuSysId2004_ObjectIdentity=ObjectIdentity
utBBSEponOnuSysId2004=_UtBBSEponOnuSysId2004_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,2,100,6))
if mibBuilder.loadTexts:utBBSEponOnuSysId2004.setStatus(_A)
_UtBBSGeponOnu_ObjectIdentity=ObjectIdentity
utBBSGeponOnu=_UtBBSGeponOnu_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,100))
if mibBuilder.loadTexts:utBBSGeponOnu.setStatus(_A)
_UtBBSGeponOnu2004_ObjectIdentity=ObjectIdentity
utBBSGeponOnu2004=_UtBBSGeponOnu2004_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,100,6))
if mibBuilder.loadTexts:utBBSGeponOnu2004.setStatus(_A)
_UtBBSGeponOnu404_ObjectIdentity=ObjectIdentity
utBBSGeponOnu404=_UtBBSGeponOnu404_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,100,7))
if mibBuilder.loadTexts:utBBSGeponOnu404.setStatus(_A)
mibBuilder.exportSymbols('UTSTARCOM-ROOT-MIB',**{'utstarcom':utstarcom,'utsRoot':utsRoot,'utsProducts':utsProducts,'utsBroadbandSwitch':utsBroadbandSwitch,'utsBBSProductSysId':utsBBSProductSysId,'utBBSEponOnuSysId':utBBSEponOnuSysId,'utBBSEponOnuSysId2004':utBBSEponOnuSysId2004,'utBBSGeponOnu':utBBSGeponOnu,'utBBSGeponOnu2004':utBBSGeponOnu2004,'utBBSGeponOnu404':utBBSGeponOnu404})