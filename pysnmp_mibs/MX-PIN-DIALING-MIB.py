_L='pinDialingGroupVer1'
_K='pinDialingDelay'
_J='pinDialingPin'
_I='pinDialingEnable'
_H='Unsigned32'
_G='MxEnableState'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='MX-PIN-DIALING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pinDialingMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,90))
if mibBuilder.loadTexts:pinDialingMIB.setRevisions(('2006-03-06 00:00','2004-08-19 00:00'))
_PinDialingMIBObjects_ObjectIdentity=ObjectIdentity
pinDialingMIBObjects=_PinDialingMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,90,1))
_PinDialingIfTable_Object=MibTable
pinDialingIfTable=_PinDialingIfTable_Object((1,3,6,1,4,1,4935,99,90,1,10))
if mibBuilder.loadTexts:pinDialingIfTable.setStatus(_A)
_PinDialingIfEntry_Object=MibTableRow
pinDialingIfEntry=_PinDialingIfEntry_Object((1,3,6,1,4,1,4935,99,90,1,10,1))
pinDialingIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pinDialingIfEntry.setStatus(_A)
class _PinDialingEnable_Type(MxEnableState):defaultValue=0
_PinDialingEnable_Type.__name__=_G
_PinDialingEnable_Object=MibTableColumn
pinDialingEnable=_PinDialingEnable_Object((1,3,6,1,4,1,4935,99,90,1,10,1,10),_PinDialingEnable_Type())
pinDialingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pinDialingEnable.setStatus(_A)
class _PinDialingPin_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PinDialingPin_Type.__name__=_D
_PinDialingPin_Object=MibTableColumn
pinDialingPin=_PinDialingPin_Object((1,3,6,1,4,1,4935,99,90,1,10,1,20),_PinDialingPin_Type())
pinDialingPin.setMaxAccess(_C)
if mibBuilder.loadTexts:pinDialingPin.setStatus(_A)
class _PinDialingDelay_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_PinDialingDelay_Type.__name__=_H
_PinDialingDelay_Object=MibTableColumn
pinDialingDelay=_PinDialingDelay_Object((1,3,6,1,4,1,4935,99,90,1,10,1,30),_PinDialingDelay_Type())
pinDialingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pinDialingDelay.setStatus(_A)
_PinDialingConformance_ObjectIdentity=ObjectIdentity
pinDialingConformance=_PinDialingConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,90,2))
_PinDialingCompliances_ObjectIdentity=ObjectIdentity
pinDialingCompliances=_PinDialingCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,90,2,1))
_PinDialingGroups_ObjectIdentity=ObjectIdentity
pinDialingGroups=_PinDialingGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,90,2,2))
pinDialingGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,90,2,2,1))
pinDialingGroupVer1.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:pinDialingGroupVer1.setStatus(_A)
pinDialingBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,90,2,1,1))
pinDialingBasicComplVer1.setObjects((_B,_L))
if mibBuilder.loadTexts:pinDialingBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pinDialingMIB':pinDialingMIB,'pinDialingMIBObjects':pinDialingMIBObjects,'pinDialingIfTable':pinDialingIfTable,'pinDialingIfEntry':pinDialingIfEntry,_I:pinDialingEnable,_J:pinDialingPin,_K:pinDialingDelay,'pinDialingConformance':pinDialingConformance,'pinDialingCompliances':pinDialingCompliances,'pinDialingBasicComplVer1':pinDialingBasicComplVer1,'pinDialingGroups':pinDialingGroups,_L:pinDialingGroupVer1})