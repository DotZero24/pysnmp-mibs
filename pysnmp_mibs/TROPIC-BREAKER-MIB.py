_L='tnPowerFilterGroup'
_K='tnPowerFilterCardPower'
_J='tnPowerFilterAmpRating'
_I='read-only'
_H='tnSlotIndex'
_G='TROPIC-SLOT-MIB'
_F='tnShelfIndex'
_E='TROPIC-SHELF-MIB'
_D='Integer32'
_C='OctetString'
_B='TROPIC-BREAKER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnBreakerMIB,tnMiscModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnBreakerMIB','tnMiscModules')
tnShelfIndex,=mibBuilder.importSymbols(_E,_F)
tnSlotIndex,=mibBuilder.importSymbols(_G,_H)
tnBreakerMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,5,2))
if mibBuilder.loadTexts:tnBreakerMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2013-05-21 12:00','2012-09-13 12:00','2011-05-23 12:00','2011-04-14 12:00','2010-10-18 12:00','2009-08-13 12:00'))
_TnBreakerConf_ObjectIdentity=ObjectIdentity
tnBreakerConf=_TnBreakerConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,2,1))
_TnBreakerGroups_ObjectIdentity=ObjectIdentity
tnBreakerGroups=_TnBreakerGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,2,1,1))
_TnBreakerCompliances_ObjectIdentity=ObjectIdentity
tnBreakerCompliances=_TnBreakerCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,2,1,2))
_TnBreakerObjs_ObjectIdentity=ObjectIdentity
tnBreakerObjs=_TnBreakerObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,2,2))
_TnBreakerBasics_ObjectIdentity=ObjectIdentity
tnBreakerBasics=_TnBreakerBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,2,2,1))
_TnPowerFilterTable_Object=MibTable
tnPowerFilterTable=_TnPowerFilterTable_Object((1,3,6,1,4,1,7483,2,2,5,2,2,1,2))
if mibBuilder.loadTexts:tnPowerFilterTable.setStatus(_A)
_TnPowerFilterEntry_Object=MibTableRow
tnPowerFilterEntry=_TnPowerFilterEntry_Object((1,3,6,1,4,1,7483,2,2,5,2,2,1,2,1))
tnPowerFilterEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:tnPowerFilterEntry.setStatus(_A)
class _TnPowerFilterAmpRating_Type(Integer32):defaultValue=0
_TnPowerFilterAmpRating_Type.__name__=_D
_TnPowerFilterAmpRating_Object=MibTableColumn
tnPowerFilterAmpRating=_TnPowerFilterAmpRating_Object((1,3,6,1,4,1,7483,2,2,5,2,2,1,2,1,1),_TnPowerFilterAmpRating_Type())
tnPowerFilterAmpRating.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPowerFilterAmpRating.setStatus(_A)
if mibBuilder.loadTexts:tnPowerFilterAmpRating.setUnits('1/10 amps')
class _TnPowerFilterCardPower_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_TnPowerFilterCardPower_Type.__name__=_C
_TnPowerFilterCardPower_Object=MibTableColumn
tnPowerFilterCardPower=_TnPowerFilterCardPower_Object((1,3,6,1,4,1,7483,2,2,5,2,2,1,2,1,2),_TnPowerFilterCardPower_Type())
tnPowerFilterCardPower.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPowerFilterCardPower.setStatus(_A)
if mibBuilder.loadTexts:tnPowerFilterCardPower.setUnits('watts')
tnPowerFilterGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,5,2,1,1,2))
tnPowerFilterGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:tnPowerFilterGroup.setStatus(_A)
tnBreakerCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,5,2,1,2,1))
tnBreakerCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:tnBreakerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnBreakerMibModule':tnBreakerMibModule,'tnBreakerConf':tnBreakerConf,'tnBreakerGroups':tnBreakerGroups,_L:tnPowerFilterGroup,'tnBreakerCompliances':tnBreakerCompliances,'tnBreakerCompliance':tnBreakerCompliance,'tnBreakerObjs':tnBreakerObjs,'tnBreakerBasics':tnBreakerBasics,'tnPowerFilterTable':tnPowerFilterTable,'tnPowerFilterEntry':tnPowerFilterEntry,_J:tnPowerFilterAmpRating,_K:tnPowerFilterCardPower})