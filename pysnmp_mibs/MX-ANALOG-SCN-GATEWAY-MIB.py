_N='analogScnGwDialingVer1'
_M='analogScnGwDialEnable'
_L='analogScnGwDtmfDuration'
_K='analogScnGwInterDigitDialDelay'
_J='analogScnGwPreDialDelay'
_I='analogScnGwDialPrefix'
_H='MxEnableState'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='Unsigned32'
_C='read-write'
_B='MX-ANALOG-SCN-GATEWAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
analogScnGwMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,85))
if mibBuilder.loadTexts:analogScnGwMIB.setRevisions(('2005-10-27 00:00','2003-08-12 00:00','2003-03-25 00:00','2003-02-25 00:00'))
_AnalogScnGwMIBObjects_ObjectIdentity=ObjectIdentity
analogScnGwMIBObjects=_AnalogScnGwMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,85,1))
_AnalogScnGwIfDialingTable_Object=MibTable
analogScnGwIfDialingTable=_AnalogScnGwIfDialingTable_Object((1,3,6,1,4,1,4935,15,85,1,10))
if mibBuilder.loadTexts:analogScnGwIfDialingTable.setStatus(_A)
_AnalogScnGwIfDialingEntry_Object=MibTableRow
analogScnGwIfDialingEntry=_AnalogScnGwIfDialingEntry_Object((1,3,6,1,4,1,4935,15,85,1,10,5))
analogScnGwIfDialingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:analogScnGwIfDialingEntry.setStatus(_A)
class _AnalogScnGwDialPrefix_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AnalogScnGwDialPrefix_Type.__name__=_E
_AnalogScnGwDialPrefix_Object=MibTableColumn
analogScnGwDialPrefix=_AnalogScnGwDialPrefix_Object((1,3,6,1,4,1,4935,15,85,1,10,5,10),_AnalogScnGwDialPrefix_Type())
analogScnGwDialPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:analogScnGwDialPrefix.setStatus(_A)
class _AnalogScnGwPreDialDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AnalogScnGwPreDialDelay_Type.__name__=_D
_AnalogScnGwPreDialDelay_Object=MibTableColumn
analogScnGwPreDialDelay=_AnalogScnGwPreDialDelay_Object((1,3,6,1,4,1,4935,15,85,1,10,5,15),_AnalogScnGwPreDialDelay_Type())
analogScnGwPreDialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:analogScnGwPreDialDelay.setStatus(_A)
class _AnalogScnGwInterDigitDialDelay_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_AnalogScnGwInterDigitDialDelay_Type.__name__=_D
_AnalogScnGwInterDigitDialDelay_Object=MibTableColumn
analogScnGwInterDigitDialDelay=_AnalogScnGwInterDigitDialDelay_Object((1,3,6,1,4,1,4935,15,85,1,10,5,20),_AnalogScnGwInterDigitDialDelay_Type())
analogScnGwInterDigitDialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:analogScnGwInterDigitDialDelay.setStatus(_A)
class _AnalogScnGwDtmfDuration_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_AnalogScnGwDtmfDuration_Type.__name__=_D
_AnalogScnGwDtmfDuration_Object=MibTableColumn
analogScnGwDtmfDuration=_AnalogScnGwDtmfDuration_Object((1,3,6,1,4,1,4935,15,85,1,10,5,25),_AnalogScnGwDtmfDuration_Type())
analogScnGwDtmfDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:analogScnGwDtmfDuration.setStatus(_A)
class _AnalogScnGwDialEnable_Type(MxEnableState):defaultValue=1
_AnalogScnGwDialEnable_Type.__name__=_H
_AnalogScnGwDialEnable_Object=MibTableColumn
analogScnGwDialEnable=_AnalogScnGwDialEnable_Object((1,3,6,1,4,1,4935,15,85,1,10,5,75),_AnalogScnGwDialEnable_Type())
analogScnGwDialEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:analogScnGwDialEnable.setStatus(_A)
_AnalogScnGwConformance_ObjectIdentity=ObjectIdentity
analogScnGwConformance=_AnalogScnGwConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,85,5))
_AnalogScnGwCompliances_ObjectIdentity=ObjectIdentity
analogScnGwCompliances=_AnalogScnGwCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,85,5,1))
_AnalogScnGwGroups_ObjectIdentity=ObjectIdentity
analogScnGwGroups=_AnalogScnGwGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,85,5,5))
analogScnGwDialingVer1=ObjectGroup((1,3,6,1,4,1,4935,15,85,5,5,10))
analogScnGwDialingVer1.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:analogScnGwDialingVer1.setStatus(_A)
analogScnGwComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,85,5,1,1))
analogScnGwComplVer1.setObjects((_B,_N))
if mibBuilder.loadTexts:analogScnGwComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'analogScnGwMIB':analogScnGwMIB,'analogScnGwMIBObjects':analogScnGwMIBObjects,'analogScnGwIfDialingTable':analogScnGwIfDialingTable,'analogScnGwIfDialingEntry':analogScnGwIfDialingEntry,_I:analogScnGwDialPrefix,_J:analogScnGwPreDialDelay,_K:analogScnGwInterDigitDialDelay,_L:analogScnGwDtmfDuration,_M:analogScnGwDialEnable,'analogScnGwConformance':analogScnGwConformance,'analogScnGwCompliances':analogScnGwCompliances,'analogScnGwComplVer1':analogScnGwComplVer1,'analogScnGwGroups':analogScnGwGroups,_N:analogScnGwDialingVer1})