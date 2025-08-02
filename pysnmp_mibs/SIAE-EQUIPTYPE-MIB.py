_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
equipTypeMib=ModuleIdentity((1,3,6,1,4,1,3373,1103,501))
if mibBuilder.loadTexts:equipTypeMib.setRevisions(('2015-04-23 00:00','2014-10-29 00:00','2014-06-23 00:00','2013-04-16 00:00'))
_EquipTypeList_ObjectIdentity=ObjectIdentity
equipTypeList=_EquipTypeList_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5))
_EquipTypeUnknown_ObjectIdentity=ObjectIdentity
equipTypeUnknown=_EquipTypeUnknown_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,1))
if mibBuilder.loadTexts:equipTypeUnknown.setStatus(_A)
_EquipTypeALFO80HD_ObjectIdentity=ObjectIdentity
equipTypeALFO80HD=_EquipTypeALFO80HD_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,74))
if mibBuilder.loadTexts:equipTypeALFO80HD.setStatus(_A)
_EquipTypeALFO80HDsm_ObjectIdentity=ObjectIdentity
equipTypeALFO80HDsm=_EquipTypeALFO80HDsm_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,75))
if mibBuilder.loadTexts:equipTypeALFO80HDsm.setStatus(_A)
_EquipTypeAGS20_ObjectIdentity=ObjectIdentity
equipTypeAGS20=_EquipTypeAGS20_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,76))
if mibBuilder.loadTexts:equipTypeAGS20.setStatus(_A)
_EquipTypeALFOplus2_ObjectIdentity=ObjectIdentity
equipTypeALFOplus2=_EquipTypeALFOplus2_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,77))
if mibBuilder.loadTexts:equipTypeALFOplus2.setStatus(_A)
_EquipTypeEasyCellGateway_ObjectIdentity=ObjectIdentity
equipTypeEasyCellGateway=_EquipTypeEasyCellGateway_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,78))
if mibBuilder.loadTexts:equipTypeEasyCellGateway.setStatus(_A)
_EquipTypeALFO80HDx_ObjectIdentity=ObjectIdentity
equipTypeALFO80HDx=_EquipTypeALFO80HDx_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,79))
if mibBuilder.loadTexts:equipTypeALFO80HDx.setStatus(_A)
_EquipTypeALFOplus1_ObjectIdentity=ObjectIdentity
equipTypeALFOplus1=_EquipTypeALFOplus1_ObjectIdentity((1,3,6,1,4,1,3373,1103,1,5,80))
if mibBuilder.loadTexts:equipTypeALFOplus1.setStatus(_A)
mibBuilder.exportSymbols('SIAE-EQUIPTYPE-MIB',**{'equipTypeList':equipTypeList,'equipTypeUnknown':equipTypeUnknown,'equipTypeALFO80HD':equipTypeALFO80HD,'equipTypeALFO80HDsm':equipTypeALFO80HDsm,'equipTypeAGS20':equipTypeAGS20,'equipTypeALFOplus2':equipTypeALFOplus2,'equipTypeEasyCellGateway':equipTypeEasyCellGateway,'equipTypeALFO80HDx':equipTypeALFO80HDx,'equipTypeALFOplus1':equipTypeALFOplus1,'equipTypeMib':equipTypeMib})