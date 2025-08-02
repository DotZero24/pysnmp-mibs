_H='eltGvrpAdvertisementForbidVlanIndex'
_G='ELTEX-MES-GVRP-MIB'
_F='TruthValue'
_E='Integer32'
_D='00'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
eltMesGvrpMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,256))
if mibBuilder.loadTexts:eltMesGvrpMIB.setRevisions(('2018-01-15 00:00',))
_EltMesGvrpObjects_ObjectIdentity=ObjectIdentity
eltMesGvrpObjects=_EltMesGvrpObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,256,1))
_EltMesGvrpConfigs_ObjectIdentity=ObjectIdentity
eltMesGvrpConfigs=_EltMesGvrpConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,23,256,1,1))
_EltGvrpAdvertisementForbidVlanTable_Object=MibTable
eltGvrpAdvertisementForbidVlanTable=_EltGvrpAdvertisementForbidVlanTable_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1))
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanTable.setStatus(_A)
_EltGvrpAdvertisementForbidVlanEntry_Object=MibTableRow
eltGvrpAdvertisementForbidVlanEntry=_EltGvrpAdvertisementForbidVlanEntry_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1))
eltGvrpAdvertisementForbidVlanEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanEntry.setStatus(_A)
class _EltGvrpAdvertisementForbidVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('static',1))
_EltGvrpAdvertisementForbidVlanIndex_Type.__name__=_E
_EltGvrpAdvertisementForbidVlanIndex_Object=MibTableColumn
eltGvrpAdvertisementForbidVlanIndex=_EltGvrpAdvertisementForbidVlanIndex_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1,1),_EltGvrpAdvertisementForbidVlanIndex_Type())
eltGvrpAdvertisementForbidVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanIndex.setStatus(_A)
class _EltGvrpAdvertisementForbidVlanId1To1024_Type(OctetString):defaultHexValue=_D;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltGvrpAdvertisementForbidVlanId1To1024_Type.__name__=_B
_EltGvrpAdvertisementForbidVlanId1To1024_Object=MibTableColumn
eltGvrpAdvertisementForbidVlanId1To1024=_EltGvrpAdvertisementForbidVlanId1To1024_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1,2),_EltGvrpAdvertisementForbidVlanId1To1024_Type())
eltGvrpAdvertisementForbidVlanId1To1024.setMaxAccess(_C)
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanId1To1024.setStatus(_A)
class _EltGvrpAdvertisementForbidVlanId1025To2048_Type(OctetString):defaultHexValue=_D;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltGvrpAdvertisementForbidVlanId1025To2048_Type.__name__=_B
_EltGvrpAdvertisementForbidVlanId1025To2048_Object=MibTableColumn
eltGvrpAdvertisementForbidVlanId1025To2048=_EltGvrpAdvertisementForbidVlanId1025To2048_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1,3),_EltGvrpAdvertisementForbidVlanId1025To2048_Type())
eltGvrpAdvertisementForbidVlanId1025To2048.setMaxAccess(_C)
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanId1025To2048.setStatus(_A)
class _EltGvrpAdvertisementForbidVlanId2049To3072_Type(OctetString):defaultHexValue=_D;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltGvrpAdvertisementForbidVlanId2049To3072_Type.__name__=_B
_EltGvrpAdvertisementForbidVlanId2049To3072_Object=MibTableColumn
eltGvrpAdvertisementForbidVlanId2049To3072=_EltGvrpAdvertisementForbidVlanId2049To3072_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1,4),_EltGvrpAdvertisementForbidVlanId2049To3072_Type())
eltGvrpAdvertisementForbidVlanId2049To3072.setMaxAccess(_C)
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanId2049To3072.setStatus(_A)
class _EltGvrpAdvertisementForbidVlanId3073To4094_Type(OctetString):defaultHexValue=_D;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltGvrpAdvertisementForbidVlanId3073To4094_Type.__name__=_B
_EltGvrpAdvertisementForbidVlanId3073To4094_Object=MibTableColumn
eltGvrpAdvertisementForbidVlanId3073To4094=_EltGvrpAdvertisementForbidVlanId3073To4094_Object((1,3,6,1,4,1,35265,1,23,256,1,1,1,1,5),_EltGvrpAdvertisementForbidVlanId3073To4094_Type())
eltGvrpAdvertisementForbidVlanId3073To4094.setMaxAccess(_C)
if mibBuilder.loadTexts:eltGvrpAdvertisementForbidVlanId3073To4094.setStatus(_A)
class _EltGvrpStaticVlanEnable_Type(TruthValue):defaultValue=2
_EltGvrpStaticVlanEnable_Type.__name__=_F
_EltGvrpStaticVlanEnable_Object=MibScalar
eltGvrpStaticVlanEnable=_EltGvrpStaticVlanEnable_Object((1,3,6,1,4,1,35265,1,23,256,1,1,2),_EltGvrpStaticVlanEnable_Type())
eltGvrpStaticVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltGvrpStaticVlanEnable.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'eltMesGvrpMIB':eltMesGvrpMIB,'eltMesGvrpObjects':eltMesGvrpObjects,'eltMesGvrpConfigs':eltMesGvrpConfigs,'eltGvrpAdvertisementForbidVlanTable':eltGvrpAdvertisementForbidVlanTable,'eltGvrpAdvertisementForbidVlanEntry':eltGvrpAdvertisementForbidVlanEntry,_H:eltGvrpAdvertisementForbidVlanIndex,'eltGvrpAdvertisementForbidVlanId1To1024':eltGvrpAdvertisementForbidVlanId1To1024,'eltGvrpAdvertisementForbidVlanId1025To2048':eltGvrpAdvertisementForbidVlanId1025To2048,'eltGvrpAdvertisementForbidVlanId2049To3072':eltGvrpAdvertisementForbidVlanId2049To3072,'eltGvrpAdvertisementForbidVlanId3073To4094':eltGvrpAdvertisementForbidVlanId3073To4094,'eltGvrpStaticVlanEnable':eltGvrpStaticVlanEnable})