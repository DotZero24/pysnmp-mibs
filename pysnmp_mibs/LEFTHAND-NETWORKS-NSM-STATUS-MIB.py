_H='lefthandNetworksNsmStatusGroup'
_G='statusSNMPD'
_F='statusMessage'
_E='status'
_D='Integer32'
_C='read-only'
_B='LEFTHAND-NETWORKS-NSM-STATUS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,lhnNsm=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG-MIB','lhnModules','lhnNsm')
lhnNsmStatus,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NSM-MIB','lhnNsmStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lhnNsmStatusModule=ModuleIdentity((1,3,6,1,4,1,9804,2,1,99))
if mibBuilder.loadTexts:lhnNsmStatusModule.setRevisions(('2013-11-21 00:00','2013-06-25 00:00','2012-09-04 00:00','2011-06-21 00:00','2010-09-07 00:00','2010-07-19 00:00','2009-11-20 00:00','2009-03-10 00:00','2008-01-24 00:00'))
_LhnNsmStatusModuleConformance_ObjectIdentity=ObjectIdentity
lhnNsmStatusModuleConformance=_LhnNsmStatusModuleConformance_ObjectIdentity((1,3,6,1,4,1,9804,2,1,99,1))
_LhnNsmStatusModuleCompliances_ObjectIdentity=ObjectIdentity
lhnNsmStatusModuleCompliances=_LhnNsmStatusModuleCompliances_ObjectIdentity((1,3,6,1,4,1,9804,2,1,99,1,1))
_LhnNsmStatusModuleGroups_ObjectIdentity=ObjectIdentity
lhnNsmStatusModuleGroups=_LhnNsmStatusModuleGroups_ObjectIdentity((1,3,6,1,4,1,9804,2,1,99,1,2))
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_Status_Type.__name__=_D
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,9804,3,1,1,2,99,1),_Status_Type())
status.setMaxAccess(_C)
if mibBuilder.loadTexts:status.setStatus(_A)
_StatusMessage_Type=DisplayString
_StatusMessage_Object=MibScalar
statusMessage=_StatusMessage_Object((1,3,6,1,4,1,9804,3,1,1,2,99,2),_StatusMessage_Type())
statusMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMessage.setStatus(_A)
_StatusSNMPD_Type=DisplayString
_StatusSNMPD_Object=MibScalar
statusSNMPD=_StatusSNMPD_Object((1,3,6,1,4,1,9804,3,1,1,2,99,3),_StatusSNMPD_Type())
statusSNMPD.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSNMPD.setStatus(_A)
lefthandNetworksNsmStatusGroup=ObjectGroup((1,3,6,1,4,1,9804,2,1,99,1,2,1))
lefthandNetworksNsmStatusGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:lefthandNetworksNsmStatusGroup.setStatus(_A)
lefthandNetworksNsmStatusMibCompliance=ModuleCompliance((1,3,6,1,4,1,9804,2,1,99,1,1,1))
lefthandNetworksNsmStatusMibCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:lefthandNetworksNsmStatusMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lhnNsmStatusModule':lhnNsmStatusModule,'lhnNsmStatusModuleConformance':lhnNsmStatusModuleConformance,'lhnNsmStatusModuleCompliances':lhnNsmStatusModuleCompliances,'lefthandNetworksNsmStatusMibCompliance':lefthandNetworksNsmStatusMibCompliance,'lhnNsmStatusModuleGroups':lhnNsmStatusModuleGroups,_H:lefthandNetworksNsmStatusGroup,_E:status,_F:statusMessage,_G:statusSNMPD})