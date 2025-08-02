_L='snsAMessage'
_K='snsADaddr'
_J='snsASaddr'
_I='snsASif'
_H='snsATime'
_G='snsAicmpIndex'
_F='not-accessible'
_E='snsAIndex'
_D='Integer32'
_C='STORMSHIELD-ALARM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snsNotifications,stormshieldMIB=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','snsNotifications','stormshieldMIB')
snsAlarm=ModuleIdentity((1,3,6,1,4,1,11256,1,5))
if mibBuilder.loadTexts:snsAlarm.setRevisions(('2017-02-20 00:00',))
_SnsATable_Object=MibTable
snsATable=_SnsATable_Object((1,3,6,1,4,1,11256,1,5,0))
if mibBuilder.loadTexts:snsATable.setStatus(_A)
_SnsAEntry_Object=MibTableRow
snsAEntry=_SnsAEntry_Object((1,3,6,1,4,1,11256,1,5,0,1))
snsAEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:snsAEntry.setStatus(_A)
class _SnsAIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnsAIndex_Type.__name__=_D
_SnsAIndex_Object=MibTableColumn
snsAIndex=_SnsAIndex_Object((1,3,6,1,4,1,11256,1,5,0,1,0),_SnsAIndex_Type())
snsAIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsAIndex.setStatus(_A)
_SnsATime_Type=OctetString
_SnsATime_Object=MibTableColumn
snsATime=_SnsATime_Object((1,3,6,1,4,1,11256,1,5,0,1,1),_SnsATime_Type())
snsATime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsATime.setStatus(_A)
_SnsASif_Type=OctetString
_SnsASif_Object=MibTableColumn
snsASif=_SnsASif_Object((1,3,6,1,4,1,11256,1,5,0,1,2),_SnsASif_Type())
snsASif.setMaxAccess(_B)
if mibBuilder.loadTexts:snsASif.setStatus(_A)
_SnsADif_Type=OctetString
_SnsADif_Object=MibTableColumn
snsADif=_SnsADif_Object((1,3,6,1,4,1,11256,1,5,0,1,3),_SnsADif_Type())
snsADif.setMaxAccess(_B)
if mibBuilder.loadTexts:snsADif.setStatus(_A)
_SnsAProto_Type=OctetString
_SnsAProto_Object=MibTableColumn
snsAProto=_SnsAProto_Object((1,3,6,1,4,1,11256,1,5,0,1,4),_SnsAProto_Type())
snsAProto.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAProto.setStatus(_A)
_SnsASaddr_Type=OctetString
_SnsASaddr_Object=MibTableColumn
snsASaddr=_SnsASaddr_Object((1,3,6,1,4,1,11256,1,5,0,1,5),_SnsASaddr_Type())
snsASaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsASaddr.setStatus(_A)
_SnsADaddr_Type=OctetString
_SnsADaddr_Object=MibTableColumn
snsADaddr=_SnsADaddr_Object((1,3,6,1,4,1,11256,1,5,0,1,6),_SnsADaddr_Type())
snsADaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsADaddr.setStatus(_A)
_SnsASport_Type=Integer32
_SnsASport_Object=MibTableColumn
snsASport=_SnsASport_Object((1,3,6,1,4,1,11256,1,5,0,1,7),_SnsASport_Type())
snsASport.setMaxAccess(_B)
if mibBuilder.loadTexts:snsASport.setStatus(_A)
_SnsADport_Type=Integer32
_SnsADport_Object=MibTableColumn
snsADport=_SnsADport_Object((1,3,6,1,4,1,11256,1,5,0,1,8),_SnsADport_Type())
snsADport.setMaxAccess(_B)
if mibBuilder.loadTexts:snsADport.setStatus(_A)
_SnsASname_Type=OctetString
_SnsASname_Object=MibTableColumn
snsASname=_SnsASname_Object((1,3,6,1,4,1,11256,1,5,0,1,9),_SnsASname_Type())
snsASname.setMaxAccess(_B)
if mibBuilder.loadTexts:snsASname.setStatus(_A)
_SnsADname_Type=OctetString
_SnsADname_Object=MibTableColumn
snsADname=_SnsADname_Object((1,3,6,1,4,1,11256,1,5,0,1,10),_SnsADname_Type())
snsADname.setMaxAccess(_B)
if mibBuilder.loadTexts:snsADname.setStatus(_A)
_SnsAMessage_Type=SnmpAdminString
_SnsAMessage_Object=MibTableColumn
snsAMessage=_SnsAMessage_Object((1,3,6,1,4,1,11256,1,5,0,1,11),_SnsAMessage_Type())
snsAMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAMessage.setStatus(_A)
_SnsAicmpTable_Object=MibTable
snsAicmpTable=_SnsAicmpTable_Object((1,3,6,1,4,1,11256,1,5,1))
if mibBuilder.loadTexts:snsAicmpTable.setStatus(_A)
_SnsAicmpEntry_Object=MibTableRow
snsAicmpEntry=_SnsAicmpEntry_Object((1,3,6,1,4,1,11256,1,5,1,1))
snsAicmpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:snsAicmpEntry.setStatus(_A)
class _SnsAicmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnsAicmpIndex_Type.__name__=_D
_SnsAicmpIndex_Object=MibTableColumn
snsAicmpIndex=_SnsAicmpIndex_Object((1,3,6,1,4,1,11256,1,5,1,1,0),_SnsAicmpIndex_Type())
snsAicmpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsAicmpIndex.setStatus(_A)
_SnsAicmpTime_Type=OctetString
_SnsAicmpTime_Object=MibTableColumn
snsAicmpTime=_SnsAicmpTime_Object((1,3,6,1,4,1,11256,1,5,1,1,1),_SnsAicmpTime_Type())
snsAicmpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpTime.setStatus(_A)
_SnsAicmpSif_Type=OctetString
_SnsAicmpSif_Object=MibTableColumn
snsAicmpSif=_SnsAicmpSif_Object((1,3,6,1,4,1,11256,1,5,1,1,2),_SnsAicmpSif_Type())
snsAicmpSif.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpSif.setStatus(_A)
_SnsAicmpDif_Type=OctetString
_SnsAicmpDif_Object=MibTableColumn
snsAicmpDif=_SnsAicmpDif_Object((1,3,6,1,4,1,11256,1,5,1,1,3),_SnsAicmpDif_Type())
snsAicmpDif.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpDif.setStatus(_A)
_SnsAicmpSaddr_Type=OctetString
_SnsAicmpSaddr_Object=MibTableColumn
snsAicmpSaddr=_SnsAicmpSaddr_Object((1,3,6,1,4,1,11256,1,5,1,1,4),_SnsAicmpSaddr_Type())
snsAicmpSaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpSaddr.setStatus(_A)
_SnsAicmpDaddr_Type=OctetString
_SnsAicmpDaddr_Object=MibTableColumn
snsAicmpDaddr=_SnsAicmpDaddr_Object((1,3,6,1,4,1,11256,1,5,1,1,5),_SnsAicmpDaddr_Type())
snsAicmpDaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpDaddr.setStatus(_A)
_SnsAicmpType_Type=Integer32
_SnsAicmpType_Object=MibTableColumn
snsAicmpType=_SnsAicmpType_Object((1,3,6,1,4,1,11256,1,5,1,1,6),_SnsAicmpType_Type())
snsAicmpType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpType.setStatus(_A)
_SnsAicmpCode_Type=Integer32
_SnsAicmpCode_Object=MibTableColumn
snsAicmpCode=_SnsAicmpCode_Object((1,3,6,1,4,1,11256,1,5,1,1,7),_SnsAicmpCode_Type())
snsAicmpCode.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpCode.setStatus(_A)
_SnsAicmpSname_Type=OctetString
_SnsAicmpSname_Object=MibTableColumn
snsAicmpSname=_SnsAicmpSname_Object((1,3,6,1,4,1,11256,1,5,1,1,8),_SnsAicmpSname_Type())
snsAicmpSname.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpSname.setStatus(_A)
_SnsAicmpDname_Type=OctetString
_SnsAicmpDname_Object=MibTableColumn
snsAicmpDname=_SnsAicmpDname_Object((1,3,6,1,4,1,11256,1,5,1,1,9),_SnsAicmpDname_Type())
snsAicmpDname.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpDname.setStatus(_A)
_SnsAicmpMessage_Type=SnmpAdminString
_SnsAicmpMessage_Object=MibTableColumn
snsAicmpMessage=_SnsAicmpMessage_Object((1,3,6,1,4,1,11256,1,5,1,1,10),_SnsAicmpMessage_Type())
snsAicmpMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAicmpMessage.setStatus(_A)
snsNotification=NotificationType((1,3,6,1,4,1,11256,1,6,1))
snsNotification.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:snsNotification.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'snsAlarm':snsAlarm,'snsATable':snsATable,'snsAEntry':snsAEntry,_E:snsAIndex,_H:snsATime,_I:snsASif,'snsADif':snsADif,'snsAProto':snsAProto,_J:snsASaddr,_K:snsADaddr,'snsASport':snsASport,'snsADport':snsADport,'snsASname':snsASname,'snsADname':snsADname,_L:snsAMessage,'snsAicmpTable':snsAicmpTable,'snsAicmpEntry':snsAicmpEntry,_G:snsAicmpIndex,'snsAicmpTime':snsAicmpTime,'snsAicmpSif':snsAicmpSif,'snsAicmpDif':snsAicmpDif,'snsAicmpSaddr':snsAicmpSaddr,'snsAicmpDaddr':snsAicmpDaddr,'snsAicmpType':snsAicmpType,'snsAicmpCode':snsAicmpCode,'snsAicmpSname':snsAicmpSname,'snsAicmpDname':snsAicmpDname,'snsAicmpMessage':snsAicmpMessage,'snsNotification':snsNotification})