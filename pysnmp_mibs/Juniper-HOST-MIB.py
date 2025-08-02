_L='juniHostGroup'
_K='juniHostRowStatus'
_J='juniHostUserPassword'
_I='juniHostUserName'
_H='juniHostProtocol'
_G='juniHostIpAddress'
_F='Integer32'
_E='juniHostName'
_D='DisplayString'
_C='read-create'
_B='Juniper-HOST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
juniHostMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,33))
if mibBuilder.loadTexts:juniHostMIB.setRevisions(('2004-11-26 00:00','2002-09-16 21:44','2001-05-07 17:02','2000-01-26 00:00'))
_JuniHostObjects_ObjectIdentity=ObjectIdentity
juniHostObjects=_JuniHostObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,33,1))
_JuniHost_ObjectIdentity=ObjectIdentity
juniHost=_JuniHost_ObjectIdentity((1,3,6,1,4,1,4874,2,2,33,1,1))
_JuniHostTable_Object=MibTable
juniHostTable=_JuniHostTable_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1))
if mibBuilder.loadTexts:juniHostTable.setStatus(_A)
_JuniHostEntry_Object=MibTableRow
juniHostEntry=_JuniHostEntry_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1))
juniHostEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:juniHostEntry.setStatus(_A)
class _JuniHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_JuniHostName_Type.__name__=_D
_JuniHostName_Object=MibTableColumn
juniHostName=_JuniHostName_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,1),_JuniHostName_Type())
juniHostName.setMaxAccess('read-only')
if mibBuilder.loadTexts:juniHostName.setStatus(_A)
_JuniHostIpAddress_Type=IpAddress
_JuniHostIpAddress_Object=MibTableColumn
juniHostIpAddress=_JuniHostIpAddress_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,2),_JuniHostIpAddress_Type())
juniHostIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHostIpAddress.setStatus(_A)
class _JuniHostProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('juniHostFtp',1),('juniHostTftp',2)))
_JuniHostProtocol_Type.__name__=_F
_JuniHostProtocol_Object=MibTableColumn
juniHostProtocol=_JuniHostProtocol_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,3),_JuniHostProtocol_Type())
juniHostProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHostProtocol.setStatus(_A)
class _JuniHostUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_JuniHostUserName_Type.__name__=_D
_JuniHostUserName_Object=MibTableColumn
juniHostUserName=_JuniHostUserName_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,4),_JuniHostUserName_Type())
juniHostUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHostUserName.setStatus(_A)
class _JuniHostUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_JuniHostUserPassword_Type.__name__=_D
_JuniHostUserPassword_Object=MibTableColumn
juniHostUserPassword=_JuniHostUserPassword_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,5),_JuniHostUserPassword_Type())
juniHostUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHostUserPassword.setStatus(_A)
_JuniHostRowStatus_Type=RowStatus
_JuniHostRowStatus_Object=MibTableColumn
juniHostRowStatus=_JuniHostRowStatus_Object((1,3,6,1,4,1,4874,2,2,33,1,1,1,1,6),_JuniHostRowStatus_Type())
juniHostRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHostRowStatus.setStatus(_A)
_JuniHostMIBConformance_ObjectIdentity=ObjectIdentity
juniHostMIBConformance=_JuniHostMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,33,4))
_JuniHostMIBCompliances_ObjectIdentity=ObjectIdentity
juniHostMIBCompliances=_JuniHostMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,33,4,1))
_JuniHostMIBGroups_ObjectIdentity=ObjectIdentity
juniHostMIBGroups=_JuniHostMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,33,4,2))
juniHostGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,33,4,2,1))
juniHostGroup.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:juniHostGroup.setStatus(_A)
juniHostCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,33,4,1,1))
juniHostCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:juniHostCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniHostMIB':juniHostMIB,'juniHostObjects':juniHostObjects,'juniHost':juniHost,'juniHostTable':juniHostTable,'juniHostEntry':juniHostEntry,_E:juniHostName,_G:juniHostIpAddress,_H:juniHostProtocol,_I:juniHostUserName,_J:juniHostUserPassword,_K:juniHostRowStatus,'juniHostMIBConformance':juniHostMIBConformance,'juniHostMIBCompliances':juniHostMIBCompliances,'juniHostCompliance':juniHostCompliance,'juniHostMIBGroups':juniHostMIBGroups,_L:juniHostGroup})