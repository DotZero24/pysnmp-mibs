_K='read-only'
_J='h3cObjpZonePairRuleID'
_I='h3cObjpZonePairIPVersion'
_H='h3cObjpZonePairDstZone'
_G='h3cObjpZonePairSrcZone'
_F='Unsigned32'
_E='Integer32'
_D='OctetString'
_C='not-accessible'
_B='H3C-OBJP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cObjp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,155))
if mibBuilder.loadTexts:h3cObjp.setRevisions(('2014-03-10 15:36',))
_H3cObjpZonePairObjects_ObjectIdentity=ObjectIdentity
h3cObjpZonePairObjects=_H3cObjpZonePairObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,155,1))
_H3cObjpZonePairRunningInfoTable_Object=MibTable
h3cObjpZonePairRunningInfoTable=_H3cObjpZonePairRunningInfoTable_Object((1,3,6,1,4,1,2011,10,2,155,1,1))
if mibBuilder.loadTexts:h3cObjpZonePairRunningInfoTable.setStatus(_A)
_H3cObjpZonePairRunningInfoEntry_Object=MibTableRow
h3cObjpZonePairRunningInfoEntry=_H3cObjpZonePairRunningInfoEntry_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1))
h3cObjpZonePairRunningInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:h3cObjpZonePairRunningInfoEntry.setStatus(_A)
class _H3cObjpZonePairSrcZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cObjpZonePairSrcZone_Type.__name__=_D
_H3cObjpZonePairSrcZone_Object=MibTableColumn
h3cObjpZonePairSrcZone=_H3cObjpZonePairSrcZone_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,1),_H3cObjpZonePairSrcZone_Type())
h3cObjpZonePairSrcZone.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjpZonePairSrcZone.setStatus(_A)
class _H3cObjpZonePairDstZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cObjpZonePairDstZone_Type.__name__=_D
_H3cObjpZonePairDstZone_Object=MibTableColumn
h3cObjpZonePairDstZone=_H3cObjpZonePairDstZone_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,2),_H3cObjpZonePairDstZone_Type())
h3cObjpZonePairDstZone.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjpZonePairDstZone.setStatus(_A)
class _H3cObjpZonePairIPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_H3cObjpZonePairIPVersion_Type.__name__=_E
_H3cObjpZonePairIPVersion_Object=MibTableColumn
h3cObjpZonePairIPVersion=_H3cObjpZonePairIPVersion_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,3),_H3cObjpZonePairIPVersion_Type())
h3cObjpZonePairIPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjpZonePairIPVersion.setStatus(_A)
class _H3cObjpZonePairRuleID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cObjpZonePairRuleID_Type.__name__=_F
_H3cObjpZonePairRuleID_Object=MibTableColumn
h3cObjpZonePairRuleID=_H3cObjpZonePairRuleID_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,4),_H3cObjpZonePairRuleID_Type())
h3cObjpZonePairRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjpZonePairRuleID.setStatus(_A)
_H3cObjpZonePairMatchPacketCount_Type=Counter64
_H3cObjpZonePairMatchPacketCount_Object=MibTableColumn
h3cObjpZonePairMatchPacketCount=_H3cObjpZonePairMatchPacketCount_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,5),_H3cObjpZonePairMatchPacketCount_Type())
h3cObjpZonePairMatchPacketCount.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cObjpZonePairMatchPacketCount.setStatus(_A)
_H3cObjpZonePairLastMatchTime_Type=Unsigned32
_H3cObjpZonePairLastMatchTime_Object=MibTableColumn
h3cObjpZonePairLastMatchTime=_H3cObjpZonePairLastMatchTime_Object((1,3,6,1,4,1,2011,10,2,155,1,1,1,6),_H3cObjpZonePairLastMatchTime_Type())
h3cObjpZonePairLastMatchTime.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cObjpZonePairLastMatchTime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cObjp':h3cObjp,'h3cObjpZonePairObjects':h3cObjpZonePairObjects,'h3cObjpZonePairRunningInfoTable':h3cObjpZonePairRunningInfoTable,'h3cObjpZonePairRunningInfoEntry':h3cObjpZonePairRunningInfoEntry,_G:h3cObjpZonePairSrcZone,_H:h3cObjpZonePairDstZone,_I:h3cObjpZonePairIPVersion,_J:h3cObjpZonePairRuleID,'h3cObjpZonePairMatchPacketCount':h3cObjpZonePairMatchPacketCount,'h3cObjpZonePairLastMatchTime':h3cObjpZonePairLastMatchTime})